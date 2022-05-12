from django.urls import path
from core import views

urlpatterns = [
    path('reg_seller', views.Reg_seller.as_view()),
    path('categories', views.categories),
    path('products', views.ProductViews.as_view()),
    path('get_products', views.get_products),
    path('update_product/<int:pk>', views.ProductUpdate.as_view()),
    path('activate/<str:uid>/<str:token>/', views.ActivateUserEmail.as_view(), name='activate email')
]