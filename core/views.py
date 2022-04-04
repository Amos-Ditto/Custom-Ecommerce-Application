from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

# --> models
from core.models import (
    Seller_Details
)

# --> serializers
from core.serializers import (
    SellerDetailSerializer
)


# --> register seller
class Reg_seller(APIView):
    def post(self, request, format=None):
        data = request.data

        print(data)
        return Response({'received': 'welcome'}, status=status.HTTP_201_CREATED)