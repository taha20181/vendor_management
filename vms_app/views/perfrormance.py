from rest_framework.response import Response
from vms_app.models import *
from vms_app.serializers import VendorPerformanceSerializer
from rest_framework import status
from rest_framework.views import APIView


class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(id=vendor_id)
            
        serializer = VendorPerformanceSerializer(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)