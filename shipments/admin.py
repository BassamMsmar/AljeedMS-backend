from django.contrib import admin
from .models import Shipments

class ShipmentsAdmin(admin.ModelAdmin):
    list_display = ['driver', 'client', 'invoice_number', 'bill_number']

# Register your models here.
admin.site.register(Shipments, ShipmentsAdmin)