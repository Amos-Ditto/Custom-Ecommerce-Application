from rest_framework import serializers
from django.contrib.auth import get_user_model


from core.models import (
    Products, Seller_Details, Category
)

UserCustom = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCustom
        fields = [
            'email', 'first_name'
        ]


class SellerSerializer(serializers.ModelSerializer):

    user = CustomUserSerializer(read_only=True, source="user")
    class Meta:
        model = Seller_Details
        fields = [
            'user', 'county', 'phone_number', 'delivering'
        ]

class ProductSerializer(serializers.ModelSerializer):
    
    owner = SellerSerializer(read_only=True, source='owner')

    class Meta:
        model = Products
        fields = [
            'id', 'owner', 'name', 'describtion', 'image', 'price',
            'date_entered'
        ]