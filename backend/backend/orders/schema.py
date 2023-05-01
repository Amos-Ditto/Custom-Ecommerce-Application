import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import UserWishListItem


class TUserWishList(DjangoObjectType):
    class Meta:
        model = UserWishListItem


class Query(graphene.ObjectType):
    list_my_wishlist = graphene.List(TUserWishList)

    def resolve_list_my_wishlist(root, info):
        if info.context.user.is_authenticated:
            return UserWishListItem.objects.filter(userId=info.context.user)
        return None
