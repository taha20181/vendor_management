from django.contrib import admin

# Register your models here.

from .models.vendor import Vendor
from .models.purchase_order import PurchaseOrder
from .models.historical_perf import HistoricalPerformance


admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)