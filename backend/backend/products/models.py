from django.db import models
from django.conf import settings
from ckeditor_uploader import fields
from django.contrib.auth import get_user_model
from ..users.models import Seller

AppUser = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=250)
    dateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    categoryId = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="sub_category"
    )
    image = models.ImageField(upload_to="", blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product SubCategory"
        verbose_name_plural = "Product SubCategories"

    def __str__(self):
        return self.name

    def upload_to(self, filename):
        extension = filename.split(".")[-1]

        new_filename = f"{self.name}.{extension}"

        return f"categories/sub/{new_filename}"

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = self.upload_to(self.image.name)
        super().save(*args, **kwargs)

    @property
    def subCategoryUrl(self):
        if self.image:
            return settings.HOST_URL + self.image.url
        else:
            return ""


class Brand(models.Model):
    name = models.CharField(max_length=250)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", blank=True, null=True)

    class Meta:
        verbose_name = "Product Brand"
        verbose_name_plural = "Product Brands"

    def __str__(self):
        return self.name

    def upload_to(self, filename):
        extension = filename.split(".")[-1]

        new_filename = f"{self.name}.{extension}"

        return f"products/brands/{new_filename}"

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = self.upload_to(self.image.name)
        super().save(*args, **kwargs)

    @property
    def brandImageUrl(self):
        if self.image:
            return settings.HOST_URL + self.image.url
        else:
            return ""


class Product(models.Model):
    name = models.CharField(max_length=250)
    subCategoryId = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="product"
    )
    shop = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name="shop_product",
        blank=True,
        null=True,
    )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    inStock = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    description = fields.RichTextUploadingField(blank=True, null=True)
    searchTags = models.TextField(blank=True, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    name = models.CharField(max_length=250)
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_variant"
    )

    class Meta:
        verbose_name = "Product Variant"
        verbose_name_plural = "Product Variants"

    def __str__(self):
        return f"{self.name} | {str(self.productId.name)}"


class VariantItem(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    variantId = models.ForeignKey(
        ProductVariant, on_delete=models.CASCADE, related_name="variant"
    )

    class Meta:
        verbose_name = "Item Variant"
        verbose_name_plural = "Item Variants"

    def __str__(self):
        return f"{self.name} | {str(self.variantId)}"


class ProductImages(models.Model):
    image = models.ImageField(upload_to="")
    default = models.BooleanField(default=False)
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image"
    )

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return self.productId.name

    def upload_to(self, filename):
        extension = filename.split(".")[-1]
        name = filename.split(".")[0]

        new_filename = name + f"{self.productId.name}.{extension}"

        return f"sellers/products/{new_filename}"

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = self.upload_to(self.image.name)
        super().save(*args, **kwargs)

    @property
    def productImageUrl(self):
        if self.image:
            return settings.HOST_URL + self.image.url
        else:
            return ""


class UserWishListItem(models.Model):
    userId = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="user_wish_item"
    )
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="wish_list_item"
    )
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User Wish List"
        verbose_name_plural = "User Wish List"

    def __str__(self):
        return f"{self.userId} {self.productId.name}"
