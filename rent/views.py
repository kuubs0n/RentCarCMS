from django.http import HttpResponse
from django.template import loader
from .models import Car, Offer

def index(request):
    template = loader.get_template('rent/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def rents(request):
    offers = Offer.objects.order_by('car__brand')
    template = loader.get_template('rent/rents.html')
    context = { 'offers' : offers}
    return HttpResponse(template.render(context, request))

def details(request, offerId):
    offer = Offer.objects.filter(offerId = offerId)
    template = loader.get_template('rent/details.html')
    context = { 'offer' : offer }
    return HttpResponse(template.render(context, request))

def contact(request):
    return HttpResponse("Contact")

