from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(EventLabel)
admin.site.register(TicketFeature)
admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(TicketCategory)
admin.site.register(TicketPrice)
