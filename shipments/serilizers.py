from rest_framework import serializers
from shipments.models import Shipments

from clients.models import Clients
from drivers.models import Driver

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'




class ShipmentsSerializer(serializers.ModelSerializer):
    client = ClientsSerializer(read_only=True)
    driver = DriversSerializer(read_only=True)
    class Meta:
        model = Shipments
        fields = '__all__'