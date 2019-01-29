from django.http import HttpResponse
from django.template import loader
from .models import Car, Offer
import logging

def index(request):
    template = loader.get_template('rent/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def rents(request):
    offers = Offer.objects.order_by('car__brand')
    template = loader.get_template('rent/rents.html')
    context = { 'offers' : offers}
    return HttpResponse(template.render(context, request))

def details(request, offerUUID):
    offer = Offer.objects.get(pk=offerUUID)
    template = loader.get_template('rent/details.html')
    context = { 'offer' : offer }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('rent/contact.html')
    context = { 'offer' : "asd" }
    return HttpResponse(template.render(context, request))

