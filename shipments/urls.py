from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shipments import views
router = routers.DefaultRouter()
router.register('', views.ShipmentsViewSet)



urlpatterns = [
    path('shipments/', include(router.urls))
]






