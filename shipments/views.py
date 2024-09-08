from django.shortcuts import render
from rest_framework import viewsets


from .serilizers import ShipmentsSerializer
from .models import Shipments


# Create your views here.
class ShipmentsViewSet(viewsets.ModelViewSet):
    serializer_class = ShipmentsSerializer
    queryset = Shipments.objects.all()
