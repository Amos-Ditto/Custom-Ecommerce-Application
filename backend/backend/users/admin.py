from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
from .models import Seller


AppUser = get_user_model()


@admin.register(AppUser)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email", "full_name", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("full_name",)}),
        ("Permissions", {"fields": ("is_admin",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "full_name", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email", "full_name")
    ordering = ("full_name",)
    filter_horizontal = ()


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ["id", "userId", "shopName", "dateJoined"]
    list_filter = ["dateJoined"]


admin.site.unregister(Group)
