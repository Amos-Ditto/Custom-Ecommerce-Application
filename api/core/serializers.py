from rest_framework import serializers
from core.models import (
    Seller_Details, Category, Products
)

class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller_Details
        fields = ['id', 'user', 'county', 'town', 'phone_number', 'delivering']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'owner', 'category', 'name', 'describtion', 'image', 'price']
    
