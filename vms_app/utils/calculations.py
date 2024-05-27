from django.db.models import F
from vms_app.models import *


def on_time_delivery_rate(po_data):
    vendor_details = po_data.pop('vendor_details', None)
    vendor = None
    if vendor_details:
        vendor, _ = Vendor.objects.get_or_create(id=vendor_details['id'])
    
    total_completed = PurchaseOrder.objects.filter(vendor=vendor, status=PurchaseOrder.Status.COMPLETED).count()
    completed_on_time = PurchaseOrder.objects.filter(vendor=vendor, status=PurchaseOrder.Status.COMPLETED, delivery_date__lte=F('expected_delivery_date')).count()
    rate = round((completed_on_time / total_completed), 2)

    vendor.on_time_delivery_rate = rate
    vendor.save()


def update_avg_quality_rating(po_data):
    vendor_details = po_data.pop('vendor_details', None)
    vendor = None
    if vendor_details:
        vendor, _ = Vendor.objects.get_or_create(id=vendor_details['id'])

    if po_data['quality_rating']:
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status=PurchaseOrder.Status.COMPLETED).exclude(issue_date__isnull=True)
        total_rating = 0
        for po in completed_pos:
            total_rating += po.quality_rating
        
    vendor.quality_rating_avg = total_rating / completed_pos.count()
    vendor.save()


def update_avg_response_time(vendor):
    purchase_orders = PurchaseOrder.objects.filter(vendor=vendor).exclude(acknowledgment_date__isnull=True)
    
    response_time = []
    for po in purchase_orders:
        time_diff = po.acknowledgment_date - po.issue_date
        response_time.append(time_diff.total_seconds())
    
    total_time = sum(response_time)
    avg_response_time = total_time / len(response_time)

    vendor.average_response_time = avg_response_time
    vendor.save()


def update_fulfilment_rate(po_data):
    vendor_details = po_data.pop('vendor_details', None)
    vendor = None
    if vendor_details:
        vendor, _ = Vendor.objects.get_or_create(id=vendor_details['id'])
    
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='COMPLETED').exclude(issue_date__isnull=True).count()

    fulfillment_rate = (fulfilled_orders / total_orders) * 100

    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()