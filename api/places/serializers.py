from rest_framework import serializers

# --> models
from places.models import Regions


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = '__all__'