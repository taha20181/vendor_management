"""vendor_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Inc 
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from vms_app.views.acknowledge import acknowledge_purchase_order
from vms_app.views.vendor import VendorView
from vms_app.views.perfrormance import VendorPerformanceView
from vms_app.views.purchase_order import PurchaseOrderView


urlpatterns = [
    path('vendors/', VendorView.as_view(), name='vendor'),
    path('vendors/<int:vendor_id>/', VendorView.as_view(), name='vendor'),
    path('vendors/<int:vendor_id>/performance',  VendorPerformanceView.as_view(), name='vendor_performance'),

    path('purchase_orders/', PurchaseOrderView.as_view(), name='purchase_order'),
    path('purchase_orders/<int:po_id>/', PurchaseOrderView.as_view(), name='purchase_order'),
    path('purchase_orders/<int:po_id>/acknowledge', acknowledge_purchase_order, name='purchase_order')
    
]
