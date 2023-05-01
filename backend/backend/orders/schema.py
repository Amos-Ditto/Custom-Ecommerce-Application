import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import UserWishListItem


class TUserWishListNode(DjangoObjectType):
    class Meta:
        model = UserWishListItem
        interfaces = (relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "userId__email": ["exact"],
        }


class Query(graphene.ObjectType):
    wish_item_node = relay.Node.Field(TUserWishListNode)
    list_wish_items_node = DjangoFilterConnectionField(TUserWishListNode)


# class Query(graphene.ObjectType):

#     list_my_wishlist = graphene.List(TUserWishList)

#     def resolve_list_my_wishlist(root, info):
#         if info.context.user.is_authenticated:
#             return UserWishListItem.objects.filter(userId=info.context.user)
#         return None
