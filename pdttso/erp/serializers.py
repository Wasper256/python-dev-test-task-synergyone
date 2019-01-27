from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=30, decimal_places=2)
    date = serializers.DateTimeField()

    class Meta:
        model = Payment
        fields = ('id', 'amount', 'date')
