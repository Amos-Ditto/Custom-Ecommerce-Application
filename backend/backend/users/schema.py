import graphene
from django.conf import settings
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_file_upload.scalars import Upload
from .models import AppUser, Seller
from .forms import UserCreationForm, SellerCreationForm


class AppUserType(DjangoObjectType):
    class Meta:
        model = AppUser


class AppUserMutation(DjangoModelFormMutation):
    user = graphene.Field(AppUserType)

    class Meta:
        form_class = UserCreationForm
        group = "Users"


class SellerInput(graphene.InputObjectType):
    userId = graphene.ID(required=True)
    shopName = graphene.String(required=True)
    shopAvatar = Upload(required=True)


class SellerType(DjangoObjectType):
    class Meta:
        model = Seller

    shopAvatarUrl = graphene.String()

    def resolve_shopAvatarUrl(self, info):
        return self.shopAvatarUrl


class SellerMutation(graphene.Mutation):
    seller = graphene.Field(SellerType)

    class Arguments:
        seller_data = SellerInput(required=True)

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
    get_seller_details = graphene.Field(SellerType, id=graphene.ID(required=False))

    def resolve_get_seller_details(root, info, id=None):
        if info.context.user.is_authenticated:
            try:
                seller = Seller.objects.get(userId=info.context.user)
                return seller
            except Seller.DoesNotExist:
                raise ValueError("this seller is not registered as Seller")
        if id is not None:
            print("Id: ", id)
            try:
                seller = Seller.objects.get(userId=id)
                return seller
            except Seller.DoesNotExist:
                raise ValueError("this seller is not registered as Seller")
        else:
            raise ValueError("Please give specific details: pass user ID or Authorize")
