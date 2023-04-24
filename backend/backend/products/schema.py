import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_file_upload.scalars import Upload
from .models import (
    Category,
    SubCategory,
    Brand,
    Product,
    ProductImages,
    ProductVariant,
    VariantItem,
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


class Query(graphene.ObjectType):
    list_category = graphene.List(TCategory)
    list_sub_category = graphene.List(TSubCategory)

    def resolve_list_category(root, info):
        objs = Category.objects.all()
        return objs

    def resolve_list_sub_category(root, info):
        objs = SubCategory.objects.all()
        return objs
