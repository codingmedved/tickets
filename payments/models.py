from django.db import models
from orders.models import Order

# Create your models here.

class Payment(models.Model):
    order = models.OneToOneField(Order)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created  = models.DateTimeField(auto_now_add=True, auto_now=False)