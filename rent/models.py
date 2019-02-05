import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Car(models.Model):
    COLOR_CHOICES = (
        ("RED", "Red"), ("BLUE", "Blue"), ("BLACK", "Black"), ("WHITE", "White"), ("GREEN", "Green"), ("BROWN", "Brown"), ("ORANGE", "Orange")
    )

    carUUID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    productionYear = models.IntegerField(default=0)
    course = models.IntegerField(default=100)
    engineCapacity = models.DecimalField(max_digits=2, decimal_places=1)
    power = models.IntegerField(default=0)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default="WHITE")
    description = models.CharField(max_length=100, default="")
    photo = models.ImageField(blank=True, upload_to='gallery')

    def __str__(self):
        return self.brand + " " + self.name

class Offer(models.Model):
    offerUUID = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    available = models.BooleanField()
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.car.brand + " " + self.car.name + " " + str(self.price)

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phoneNumber = PhoneNumberField()
    city = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    latitude = models.DecimalField(blank = True, max_digits=9, decimal_places=6, null = True)
    longitude = models.DecimalField(blank = True, max_digits=9, decimal_places=6, null = True)

    def __str__(self):
        return self.city + " " + self.address

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    isReaded = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.email + " " + self.message[:20] + " " + str(self.isReaded)