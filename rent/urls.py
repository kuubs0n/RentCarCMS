from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rents', views.rents, name='rents'),
    path('contact', views.contact, name='contact'),
    path('details/<int:offerId>', views.details, name='details')
]