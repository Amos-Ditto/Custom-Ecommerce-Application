from django.urls import path
from places import views


urlpatterns = [
    path('regions', views.RegionView.as_view())
]
