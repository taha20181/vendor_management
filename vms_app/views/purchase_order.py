from datetime import datetime, timedelta
from rest_framework.response import Response
from vms_app.models import *
from vms_app.models.purchase_order import PurchaseOrder
from vms_app.serializers import PurchaseOrderSerializer
from rest_framework import status
from rest_framework.views import APIView

from vms_app.utils.calculations import on_time_delivery_rate, update_avg_quality_rating, update_avg_response_time, update_fulfilment_rate


class PurchaseOrderView(APIView):
    def get(self, request, po_id=None):
        if po_id:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            serializer = PurchaseOrderSerializer(purchase_order)
        else:
            query_params = request.query_params
            limit = int(query_params.get('limit', 10))
            offset = int(query_params.get('offset', 0))

            purchase_orders = PurchaseOrder.objects.all()
            purchase_orders = purchase_orders[offset:limit]
            purchase_orders = PurchaseOrder.objects.all()
            serializer = PurchaseOrderSerializer(purchase_orders, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, po_id):
        data = request.data
        if 'status' in data:
            if data['status'] == 'COMPLETED':
                data.update(
                    {
                        "delivery_date" : datetime.now()
                    }
                )
        purchase_order = PurchaseOrder.objects.get(id=po_id)
        serializer = PurchaseOrderSerializer(purchase_order, data=data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data['status'] == PurchaseOrder.Status.COMPLETED:
                on_time_delivery_rate(serializer.data)
                if serializer.data['quality_rating'] is not None:
                    update_avg_quality_rating(serializer.data)

            if serializer.data['status'] != '':
                update_fulfilment_rate(serializer.data)
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, po_id):
        purchase_order = PurchaseOrder.objects.get(id=po_id)
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)