from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Order)
admin.site.register(TicketStatus)
admin.site.register(TicketNumbers)
admin.site.register(TicketPurchased)
