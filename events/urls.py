from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ticket/(?P<ticket_id>\w+)/$', views.ticket, name='ticket'),

]
