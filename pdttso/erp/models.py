from django.db import models


class Payments(models.Model):
    agreement_id = models.IntegerField()
    amount = models.DecimalField(max_digits=30, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
