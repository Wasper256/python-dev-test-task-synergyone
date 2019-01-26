from django.db import models


class Payment(models.Model):
    agreement_id = models.ForeignKey('crm.Application',
                                     on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=30, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
