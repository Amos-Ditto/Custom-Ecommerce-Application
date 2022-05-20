from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
import requests

# --> models
from core.models import (
    Seller_Details, Category, Products
)

# --> serializers
from core.serializers import (
    SellerDetailSerializer, CategorySerializer, ProductSerializer
)

class ActivateUserEmail(APIView):
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, data = post_data)
        message = result.text
        return Response(message)

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
        try:
            seller = Seller_Details.objects.get(user=user)
            return Response({'seller': True})
        except Seller_Details.DoesNotExist:
            return Response({'seller': False})


@api_view(["GET"])
def categories(request):
    objs = Category.objects.all()
    serializer = CategorySerializer(objs, many=True)

    return Response(serializer.data)



class ProductViews(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        user = request.user.id
        u_details = Seller_Details.objects.get(user=user)
        data = request.data
        uploaded = {}
        uploaded['category'] = int(data['category'][0])
        uploaded['name'] = data['name']
        uploaded['describtion'] = data['describtion']
        uploaded['image'] = data['image']
        uploaded['price'] = data['price']
        uploaded['owner'] = u_details.id
        serializer = ProductSerializer(data=uploaded)
        if serializer.is_valid():
            serializer.save()
            return Response({'product': 'created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_products(request):
    user = request.user.id
    u_details = Seller_Details.objects.get(user=user)
    serailizer = Products.objects.filter(owner=u_details)
    data = ProductSerializer(serailizer, many=True, context={"request": request})
    return Response(data.data)



# --> update product 

class ProductUpdate(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_object(self, pk):
        try:
            return Products.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        obj = self.get_object(pk=pk)
        serializer = ProductSerializer(obj, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        data = request.data
        obj = self.get_object(pk=pk)
        obj.price = float(data['price'])
        obj.name = data['name']
        try:
            if data['image'] == 'undefined':
                pass
            else:
                obj.image = data['image']
        except:
            pass
        obj.save()
        serializer = ProductSerializer(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)