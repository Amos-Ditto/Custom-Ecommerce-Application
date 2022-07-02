from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# --> models
from places.models import Regions

# --> serializers
from places.serializers import RegionSerializer


class RegionView(APIView):
    def get(self, request):
        regions = Regions.objects.all()
        serializer = RegionSerializer(regions, many=True)

        return Response(serializer.data)