from django.urls import path,include
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from pictures import views

routers = DefaultRouter()

routers.register('artpiece', views.ArtPieceViewSet)

app_name = 'artpiece'

urlpatterns = [
    path('', include(routers.urls))
]