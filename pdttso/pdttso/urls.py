from django.contrib import admin
from django.urls import path, include
from erp.views import PaymentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'agreements/(?P<agreement_id>[0-9]+)/payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/v2/', include((router.urls, 'erp'), namespace='erp')),
]
