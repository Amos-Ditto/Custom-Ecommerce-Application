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
)


class TCategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "name": ["exact", "icontains", "istartswith"],
        }


class TSubCategoryNode(DjangoObjectType):
    subCategoryUrl = graphene.String()

    class Meta:
        model = SubCategory
        interfaces = (relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "name": ["exact", "icontains", "istartswith"],
            "categoryId__id": ["exact"],
            "categoryId__name": ["exact", "icontains"],
        }

    def resolve_subCategoryUrl(self, info):
        return self.subCategoryUrl


class TBrandNode(DjangoObjectType):
    brandImageUrl = graphene.String()

    class Meta:
        model = Brand
        interfaces = (relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "name": ["exact", "icontains", "istartswith"],
            "categoryId__id": ["exact"],
            "categoryId__name": ["exact", "icontains"],
        }

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
            "product_image__default": ["exact"],
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


class Query(graphene.ObjectType):
    category_node = relay.Node.Field(TCategoryNode)
    list_category_node = DjangoFilterConnectionField(TCategoryNode)
    sub_category_node = relay.Node.Field(TSubCategoryNode)
    list_sub_category_node = DjangoFilterConnectionField(TSubCategoryNode)
    brand_node = relay.Node.Field(TBrandNode)
    list_brand_node = DjangoFilterConnectionField(TBrandNode)
    product_node = relay.Node.Field(TProductNode)
    list_product_node = DjangoFilterConnectionField(TProductNode)
