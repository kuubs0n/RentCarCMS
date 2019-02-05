from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rents', views.rents, name='rents'),
    path('contact', views.contact, name='contact'),
    path('details/<uuid:offerUUID>', views.details, name='details'),
    path('message', views.message, name='message')
]