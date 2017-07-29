from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name


class City(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name


class Location(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    coordinates = models.CharField(max_length=128) #altitude and latitude in Charfield
    address = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name


class LocationImage(models.Model):
    country = models.ForeignKey(Country, blank=True, null=True, default=None)
    city = models.ForeignKey(City, blank=True, null=True, default=None)
    location = models.ForeignKey(Location, blank=True, null=True, default=None)
    image = models.ImageField(upload_to="/images/", blank=True, null=True, default=None)
    image_medium = models.ImageField(upload_to="/images_medium/", blank=True, null=True, default=None)
    image_small = models.ImageField(upload_to="/images_small/", blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id