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
        data['user'] = request.user.id
        serializer = SellerDetailSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'seller': 'created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        user = request.user
        print(user)
        try:
            seller = Seller_Details.objects.get(user=user)
            return Response({'seller': True})
        except Seller_Details.DoesNotExist:
            return Response({'seller': False})
