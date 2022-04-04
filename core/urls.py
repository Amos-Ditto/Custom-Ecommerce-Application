from django.urls import path
from core import views

urlpatterns = [
    path('reg_seller', views.Reg_seller.as_view()),
]