from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=128)
    address = models.CharField(max_length=128)