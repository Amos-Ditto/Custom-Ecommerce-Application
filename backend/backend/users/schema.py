import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_file_upload.scalars import Upload
from .models import AppUser, Seller, SellerDetails, SellerRating
from .forms import UserCreationForm


class AppUserType(DjangoObjectType):
    class Meta:
        model = AppUser


class AppUserMutation(DjangoModelFormMutation):
    user = graphene.Field(AppUserType)

    class Meta:
        form_class = UserCreationForm
        group = "Users"


class ISeller(graphene.InputObjectType):
    userId = graphene.ID(required=True)
    shopName = graphene.String(required=True)
    shopAvatar = Upload(required=True)


class TSellerNode(DjangoObjectType):
    class Meta:
        model = Seller
        filter_fields = {
            "id": ["exact"],
            "shopName": ["exact", "icontains", "istartswith"],
            "dateJoined": ["lte", "gte"],
        }
        interfaces = (relay.Node,)

    shopAvatarUrl = graphene.String()
    shopRating = graphene.List(of_type=graphene.Int)

    def resolve_shopAvatarUrl(self, info):
        return self.shopAvatarUrl

    def resolve_shopRating(self, info):
        return self.shopRating


class TSellerDetail(DjangoObjectType):
    class Meta:
        model = SellerDetails

    shopBannerUrl = graphene.String()

    def resolve_shopBannerUrl(self, info):
        return self.shopBannerUrl


class TSellerDetailNode(DjangoObjectType):
    class Meta:
        model = SellerDetails
        interfaces = (relay.Node,)

    shopBannerUrl = graphene.String()

    def resolve_shopBannerUrl(self, info):
        return self.shopBannerUrl


class TSellerRatingNode(DjangoObjectType):
    class Meta:
        model = SellerRating
        interfaces = (relay.Node,)


class SellerMutation(graphene.Mutation):
    seller = graphene.Field(TSellerNode)

    class Arguments:
        seller_data = ISeller(required=True)

    @staticmethod
    def mutate(root, info, seller_data):
        try:
            user = AppUser.objects.get(id=seller_data["userId"])
            print("User: ", user)
            seller = Seller(
                userId=user,
                shopName=seller_data["shopName"],
                shopAvatar=seller_data["shopAvatar"],
            )
            print("Seller: ", seller.shopAvatar)
            seller.save()
            return SellerMutation(seller=seller)

        except AppUser.DoesNotExist:
            raise ValueError("This User doesn't exists")


class Mutation(graphene.ObjectType):
    register_user = AppUserMutation.Field(description="Creates a new app user")
    register_seller = SellerMutation.Field(description="Create a new Seller")


class Query(graphene.ObjectType):
    shop_node = graphene.Field(TSellerNode)
    list_shop_node = DjangoFilterConnectionField(TSellerNode)
