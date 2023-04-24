from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from .manager import AppUserManager


class AppUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    full_name = models.CharField(verbose_name="full name", max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "full_name",
    ]

    class Meta:
        verbose_name = "App User"
        verbose_name_plural = "App Users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Seller(models.Model):
    userId = models.OneToOneField(
        AppUser, on_delete=models.CASCADE, related_name="seller"
    )
    shopName = models.CharField(max_length=250)
    shopAvatar = models.ImageField(upload_to="")
    dateJoined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sellers"

    def __str__(self):
        return self.shopName

    def upload_to(self, filename):
        extension = filename.split(".")[-1]

        new_filename = f"{self.shopName}.{extension}"

        return f"sellers/avatar/{new_filename}"

    def save(self, *args, **kwargs):
        if self.shopAvatar:
            self.shopAvatar.name = self.upload_to(self.shopAvatar.name)
        super().save(*args, **kwargs)

    @property
    def shopAvatarUrl(self):
        if self.shopAvatar:
            return settings.HOST_URL + self.shopAvatar.url
        else:
            return ""


class SellerDetails(models.Model):
    sellerId = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="seller_detail"
    )
    description = models.TextField(blank=True, null=True)
    bannerImage = models.ImageField(upload_to="")

    class Meta:
        verbose_name = "Seller Details"
        verbose_name_plural = "Seller Details"

    def __str__(self):
        return "Shop -> " + self.sellerId.shopName

    def upload_to(self, filename):
        extension = filename.split(".")[-1]

        new_filename = f"{self.sellerId.shopName}.{extension}"

        return f"sellers/banners/{new_filename}"

    def save(self, *args, **kwargs):
        if self.bannerImage:
            self.bannerImage.name = self.upload_to(self.bannerImage.name)
        super().save(*args, **kwargs)

    @property
    def shopBannerUrl(self):
        if self.bannerImage:
            return settings.HOST_URL + self.bannerImage.url
        else:
            return ""
