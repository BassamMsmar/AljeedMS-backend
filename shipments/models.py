from django.db import models
from clients.models import Clients
from drivers.models import Driver
# Create your models here.
STATUS = (
    ('Shipped', _('Shipped')),
    ('Delivered', _('Delivered')),
)


class Shipments(models.Model):
    client = models.ForeignKey(
        Clients, on_delete=models.CASCADE, related_name='shipments_clients')
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, related_name='driver_clients')
    destination = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    bill_number = models.CharField(max_length=200)
    invoice_number = models.CharField(max_length=200)
    status = models.TextField(
        choices=STATUS, null=True, blank=True, default=STATUS[0][0])

    def __str__(self):
        return self.name
