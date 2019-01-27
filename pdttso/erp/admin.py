from django.contrib import admin

from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'agreement_id', 'date')
    list_filter = ('amount', 'agreement_id')


admin.site.register(Payment, PaymentAdmin)
