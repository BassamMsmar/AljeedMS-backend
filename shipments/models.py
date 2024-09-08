from django.db import models
from datetime import timedelta
from clients.models import Clients
from drivers.models import Driver

STATUS = (
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_delivery_date = models.DateField(
        editable=False, null=True, blank=True)  # New field

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set the date when the object is first created
            if self.created_at:
                self.expected_delivery_date = self.created_at.date() + timedelta(days=3)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bill_number
