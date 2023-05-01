from django.contrib import admin
from .models import UserWishListItem, CartItem, Order


@admin.register(UserWishListItem)
class UserWishListAdmin(admin.ModelAdmin):
    list_display = ["id", "userId", "productId"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["id", "userId", "productId", "quantity", "dateAdded"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "paidAmount",
        "dateCreated",
        "isPaid",
        "paidAt",
    ]
