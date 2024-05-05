from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if isinstance(exc, ObjectDoesNotExist):
        return Response(
            {
                "status": "error", 
                "message" : "Data with the given id does not exist."
            }, status=404)
    return response
