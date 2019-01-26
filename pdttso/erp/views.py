from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404
from .serializers import PaymentSerializer
from .models import Payment
from rest_framework.response import Response


class PaymentViewSet(viewsets.ViewSet):
    def list(self, request, agreement_id):
        queryset = Payment.objects.filter(agreement_id=agreement_id)
        serializer = PaymentSerializer(queryset, many=True)
        print(agreement_id)
        return Response(serializer.data)

