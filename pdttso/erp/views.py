from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def list(self, request, agreement_id):
        queryset = Payment.objects.filter(agreement_id__id=agreement_id)
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)
