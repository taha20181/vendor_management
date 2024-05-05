from django.db import models

from vms_app.models.base import BaseModel
from vms_app.models.vendor import Vendor

# Create your models here.


class PurchaseOrder(BaseModel):
    class Status(models.TextChoices):
        PENDING = 'PENDING'
        COMPLETED = 'COMPLETED'
        CANCELLED = 'CANCELLED'
    
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery_date = models.DateTimeField()
    delivery_date = models.DateTimeField(blank=True, null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)