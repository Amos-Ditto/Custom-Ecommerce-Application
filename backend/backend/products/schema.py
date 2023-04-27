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


class TProductPaginate(graphene.ObjectType):
    rows = graphene.List(TProduct)
    total_rows = graphene.Int()
    current_page = graphene.Int()
    next_page = graphene.String()
    prev_page = graphene.String()


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
    list_my_wishlist = graphene.List(TUserWishList)
    page_list_product = graphene.Field(
        TProductPaginate, page=graphene.Int(), page_size=graphene.Int()
    )
    # filters
    filter_products = graphene.List(TProductPaginate, cat=graphene.String())

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

    # Paginated resolvers
    def resolve_page_list_product(root, info, page=1, page_size=10):
        queryset = Product.objects.all()
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

    def resolve_filter_products(root, info, cat=None):
        return None
