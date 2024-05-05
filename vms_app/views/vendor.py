from rest_framework.response import Response
from vms_app.models import *
from vms_app.serializers import VendorSerializer
from rest_framework import status
from rest_framework.views import APIView


class VendorView(APIView):
    def get(self, request, vendor_id=None):
        if vendor_id:
            vendor = Vendor.objects.get(id=vendor_id)
            serializer = VendorSerializer(vendor)
        else:
            query_params = request.query_params
            limit = int(query_params.get('limit', 10))
            offset = int(query_params.get('offset', 0))

            vendors = Vendor.objects.all()
            vendors = vendors[offset:limit]
            serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, vendor_id):
        vendor = Vendor.objects.get(id=vendor_id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, vendor_id):
        vendor = Vendor.objects.get(id=vendor_id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)