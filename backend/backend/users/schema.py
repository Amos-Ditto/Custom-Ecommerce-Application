import graphene
from graphene import relay
from graphene_django import DjangoObjectType
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


class TSeller(DjangoObjectType):
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


class TSellerRating(DjangoObjectType):
    class Meta:
        model = SellerRating


class TSellerPaginate(graphene.ObjectType):
    rows = graphene.List(TSeller)
    total_rows = graphene.Int()
    current_page = graphene.Int()
    next_page = graphene.String()
    prev_page = graphene.String()


class SellerMutation(graphene.Mutation):
    seller = graphene.Field(TSeller)

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
    get_seller_details = graphene.Field(TSeller, id=graphene.ID(required=False))
    list_shop = graphene.List(TSeller)
    page_list_shops = graphene.Field(
        TSellerPaginate, page=graphene.Int(), page_size=graphene.Int()
    )

    def resolve_get_seller_details(root, info, id=None):
        if info.context.user.is_authenticated:
            try:
                seller = Seller.objects.get(userId=info.context.user)
                return seller
            except Seller.DoesNotExist:
                raise ValueError("this seller is not registered as Seller")
        elif id is not None:
            print("Id: ", id)
            try:
                seller = Seller.objects.get(userId=id)
                return seller
            except Seller.DoesNotExist:
                raise ValueError("this seller is not registered as Seller")
        else:
            raise ValueError("Please give specific details: pass user ID or Authorize")

    def resolve_list_shop(root, info):
        shops = Seller.objects.all()
        return shops

    # Paginated resolvers
    def resolve_page_list_shops(root, info, page=1, page_size=10):
        queryset = Seller.objects.all()
        total_rows = queryset.count()

        # pagination values
        skip = (page - 1) * page_size
        limit = page_size + skip
        rows = queryset[skip:limit]

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if limit < total_rows else None

        return {
            "rows": rows,
            "total_rows": total_rows,
            "current_page": page,
            "next_page": next_page,
            "prev_page": prev_page,
        }
