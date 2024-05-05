from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from vms_app.models.purchase_order import PurchaseOrder
from vms_app.utils.calculations import update_avg_response_time

@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    purchase_order = PurchaseOrder.objects.get(id=po_id)
    purchase_order.acknowledgment_date = datetime.now()
    purchase_order.save()
    update_avg_response_time(purchase_order.vendor)

    return Response({"message": "Purchase Order acknowledged successfully!"}, status=status.HTTP_200_OK)
