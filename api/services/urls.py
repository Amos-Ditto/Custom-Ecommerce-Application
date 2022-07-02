from django.urls import path
from .views import requests

urlpatterns = [
    path('categories/', requests.CategoryView.as_view()),
    path('dashboard/', requests.DashBoardProductsView.as_view()),
]