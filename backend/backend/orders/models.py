from django.db import models
from django.contrib.auth import get_user_model
from backend.users.models import Seller
from backend.products.models import Product, VariantItem

AppUser = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(email="deleted@mail.com")[0]


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


class CartItem(models.Model):
    userId = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="user_cart"
    )
    productId = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_product"
    )
    variant = models.ForeignKey(
        VariantItem,
        on_delete=models.CASCADE,
        related_name="cart_variant",
        blank=True,
        null=True,
    )
    quantity = models.IntegerField(default=1)
    dateAdded = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Item"

    def __str__(self):
        return f"{self.userId.email} {self.productId.name}"


class Order(models.Model):
    user = models.ForeignKey(
        AppUser, on_delete=models.SET(get_sentinel_user), related_name="orders"
    )
    items = models.ManyToManyField(CartItem, related_name="order_items")
    paidAmount = models.FloatField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {str(self.id)} - {self.user.email}"
