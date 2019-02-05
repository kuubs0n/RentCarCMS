from django.http import HttpResponse
from django.template import loader
from .models import Car, Offer, Message, Contact
import logging
import json

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
    contact = Contact.objects.all()[:1].get()
    template = loader.get_template('rent/contact.html')
    context = { 'contact' : contact }
    return HttpResponse(template.render(context, request))

def message(request):
    POST = json.loads(request.body)
    message = Message(
        email = POST['email'],
        name = POST['name'],
        message = POST['message'],
        isReaded = POST['isReaded']
    )
    message.save()
    template = loader.get_template('rent/contact.html')
    context = { '' : ""}
    return HttpResponse(template.render(context, request))