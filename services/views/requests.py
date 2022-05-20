from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


from core.models import (
    Products, Category
)
from core.serializers import (
    CategorySerializer
)


class CategoryView(APIView):

    def get(self, request):

        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)