from rest_framework.response import Response
from vms_app.models import *
from vms_app.serializers import VendorPerformanceSerializer
from rest_framework import status
from rest_framework.views import APIView


def response(data, status, headers=None):
    resp = {
        "status" : "success" if status < 400 else "error",
        "data" : data
    }
    return Response(data=resp, status=status, headers=headers)


def response_with_message(message, status, headers=None):
    resp = {
        "status" : "success" if status < 400 else "error",
        "message" : message
    }
    return Response(data=resp, status=status, headers=headers)


class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        vendor = Vendor.objects.get(id=vendor_id)
            
        serializer = VendorPerformanceSerializer(vendor)
        return response(serializer.data, 200)