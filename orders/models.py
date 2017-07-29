from django.db import models
from events.models import Ticket, TicketPrice
from django.contrib.auth.models import User


class TicketStatus(models.Model):
    name  = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)


class TicketNumbers(models.Model):
    ticket_price = models.ForeignKey(Ticket)
    date = models.DateField()
    nmb_initial = models.IntegerField()
    nmb_current = models.IntegerField() #initially equeals to nmb_initial


class Order(models.Model):
    user = models.ForeignKey(User)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class TicketPurchased(models.Model):
    order = models.ForeignKey(Order)
    ticket_price = models.ForeignKey(TicketPrice)
    date = models.DateField()#to what date you buy it
    price = models.DecimalField(max_digits=10, decimal_places=2)
    nmb =  models.IntegerField()
    price_total = models.DecimalField(max_digits=10, decimal_places=2) #price*nmb
    status = models.ForeignKey(TicketStatus) #if more than 10 minutes in new status then cancel and return self.nmb to nmb_current on TicketNumber model
    created = models.DateTimeField(auto_now_add=True, auto_now=False)