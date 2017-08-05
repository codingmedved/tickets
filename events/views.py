from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from django.contrib import messages


def home(request):
    tickets = Ticket.objects.all()
    return render(request, 'events/home.html', locals())


def ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    top_five_tickets = Ticket.objects.all().exclude(id=ticket_id).order_by("-rating")[:5]

        # ticket.get_is_ticket_purchased(user)

    is_ticket_purchased = True

    if request.POST:
        data = request.POST
        print(data)
        print (data.get("rating"))
        rating = data.get("rating")
        ticket.rating = rating
        ticket.save(force_update=True)


    return render(request, 'events/ticket.html', locals())