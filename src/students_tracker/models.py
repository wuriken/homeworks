from django.db import models


class Logger(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=256)
    execution_time = models.DecimalField(max_digits=7, decimal_places=4)
    created = models.DateTimeField(auto_now_add=True)
