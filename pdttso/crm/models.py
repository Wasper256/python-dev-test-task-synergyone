from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=50)
    agreement_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
