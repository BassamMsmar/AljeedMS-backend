from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters


from .serilizers import ShipmentsSerializer
from .models import Shipments


# Create your views here.
class ShipmentsViewSet(viewsets.ModelViewSet):
    serializer_class = ShipmentsSerializer
    queryset = Shipments.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['client__name', 'driver__name', 'status']
