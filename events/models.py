from django.db import models
from django.contrib.auth.models import User
from locations.models import Location


# Create your models here.

# class Label(models.Model):
#     user = models.OneToOneField(User)
#     city = models.ForeignKey(City)
#     date_birth = models.DateField()
#     age = models.IntegerField()
#     description = models.TextField(blank=True, null=True)
#     avatar = models.ImageField(upload_to='avatars/')

"""
comment
"""
class EventLabel(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)


class TicketFeature(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)


class Ticket(models.Model):
    locations = models.ManyToManyField(Location)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True)
    review_nmb = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    lables = models.ManyToManyField(EventLabel, blank=True)

    #overview section
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    time_best_start = models.TimeField(blank=True, null=True)
    time_best_end = models.TimeField(blank=True, null=True)
    highlights = models.TextField()
    description = models.TextField()

    #tickets
    ticket_feature = models.ManyToManyField(TicketFeature, blank=True)
    how_to_use = models.TextField()

    additional_info = models.TextField()
    insider_tip = models.TextField()

    def __str__(self):
        return "%s" % self.title

    # def get_is_ticket_purchased(self, user):




class Review(models.Model):
    ticket = models.ForeignKey(Ticket)
    user = models.ForeignKey(User)
    text = models.TextField()
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class TicketCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    is_active = models.BooleanField(default=True)


class TicketPrice(models.Model):
    ticket = models.ForeignKey(Ticket)
    category = models.ForeignKey(TicketCategory)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.ticket.title, self.category.name)

