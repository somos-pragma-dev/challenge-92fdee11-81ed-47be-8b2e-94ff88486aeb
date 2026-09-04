from django.db import models

class Loan(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20)