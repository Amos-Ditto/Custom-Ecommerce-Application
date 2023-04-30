import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload
from graphene_django.filter import DjangoFilterConnectionField
from .models import (
    Category,
    SubCategory,
    Brand,
    Product,
    ProductImages,
    ProductVariant,
    VariantItem,
    UserWishListItem,
)


class TCategory(DjangoObjectType):
    class Meta:
        model = Category


class TSubCategory(DjangoObjectType):
    class Meta:
        model = SubCategory

    subCategoryUrl = graphene.String()

    def resolve_subCategoryUrl(self, info):
        return self.subCategoryUrl


class TBrand(DjangoObjectType):
    class Meta:
        model = Brand

    brandImageUrl = graphene.String()

    def resolve_brandImageUrl(self, info):
        return self.brandImageUrl


class TProduct(DjangoObjectType):
    class Meta:
        model = Product


class TProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {
            "id": ["exact"],
            "name": ["exact", "icontains", "istartswith"],
            "shop__id": ["exact"],
            "shop__shopName": ["exact", "icontains"],
            "subCategoryId__id": ["exact"],
            "subCategoryId__categoryId__id": ["exact"],
            "subCategoryId__name": ["exact", "icontains"],
            "subCategoryId__categoryId__name": ["exact", "icontains"],
            "price": ["lte", "gte"],
            "discount": ["lte", "gte"],
            "searchTags": ["icontains"],
        }
        interfaces = (relay.Node,)


class TProductVariant(DjangoObjectType):
    class Meta:
        model = ProductVariant


class TVariantItem(DjangoObjectType):
    class Meta:
        model = VariantItem


class TProductImages(DjangoObjectType):
    class Meta:
        model = ProductImages

    productImageUrl = graphene.String()

    def resolve_productImageUrl(self, info):
        return self.productImageUrl


class TUserWishList(DjangoObjectType):
    class Meta:
        model = UserWishListItem


class Query(graphene.ObjectType):
    list_category = graphene.List(TCategory)
    list_sub_category = graphene.List(TSubCategory)
    list_brand = graphene.List(TBrand)
    list_products = graphene.List(TProduct)
    list_product_node = relay.Node.Field(TProductNode)
    all_list_product_node = DjangoFilterConnectionField(TProductNode)
    list_my_wishlist = graphene.List(TUserWishList)

    def resolve_list_category(root, info):
        objs = Category.objects.all()
        return objs

    def resolve_list_sub_category(root, info):
        objs = SubCategory.objects.all()
        return objs

    def resolve_list_brand(root, info):
        objs = Brand.objects.all()
        return objs

    def resolve_list_products(root, info):
        products = Product.objects.filter(product_image__default=True)
        return products

    def resolve_list_my_wishlist(root, info):
        if info.context.user.is_authenticated:
            return UserWishListItem.objects.filter(userId=info.context.user)
        return None
