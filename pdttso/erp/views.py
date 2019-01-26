from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import PaymentSerializer
from .models import Payment
from rest_framework.response import Response


class PaymentViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def list(self, request, agreement_id):
        queryset = Payment.objects.filter(agreement_id=agreement_id)
        serializer = PaymentSerializer(queryset, many=True)
        print(agreement_id)
        return Response(serializer.data)

