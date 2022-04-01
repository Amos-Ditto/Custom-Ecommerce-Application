from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# ----------> Custom User model and manager --->

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,
            password=None
        ):
        if not email:
            raise ValueError('You must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',
                max_length=255,
                unique=True
            )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

# --------------------- End of Custom user and its manager ------->

class Seller_Details(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    county = models.CharField(max_length=100, null=True)
    town = models.CharField(max_length=150, null=True)
    phone_number = models.IntegerField(null=True)
    active = models.BooleanField(default=True, null=True)
    
    class Meta:
        verbose_name = 'Seller Details'
        verbose_name_plural = 'Seller Details'

    def __str__(self):
        return '{} | {}'.format(str(self.user.email), str(self.phone_number))


class Category(models.Model):
    name = models.CharField(max_length=400)
    code = models.FloatField()
    describtion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"



class Products(models.Model):
    owner = models.ForeignKey(Seller_Details, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    describtion = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    premium = models.BooleanField(default=False)
    date_entered = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"