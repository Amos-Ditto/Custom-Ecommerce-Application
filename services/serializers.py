from rest_framework import serializers

from core.models import (
    Products, Seller_Details, Category, CustomUser
)


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
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