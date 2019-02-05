from django.contrib import admin

from .models import Car, Offer, Message, Contact

admin.site.register(Car)
admin.site.register(Offer)
admin.site.register(Message)
admin.site.register(Contact)