from rest_framework import serializers
from core.models import (
    Seller_Details
)

class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller_Details
        fields = ['user', 'county', 'town', 'phone_number', 'delivering']
