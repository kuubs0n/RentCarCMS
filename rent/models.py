from django.db import models

class Car(models.Model):
    COLOR_CHOICES = (
        ("RED", "Red"), ("BLUE", "Blue"), ("BLACK", "Black"), ("WHITE", "White"), ("GREEN", "Green"), ("BROWN", "Brown"), ("ORANGE", "Orange")
    )

    carId = models.AutoField(primary_key=True, default=0)
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    productionYear = models.DateTimeField()
    course = models.IntegerField()
    engineCapacity = models.DecimalField(max_digits=2, decimal_places=1)
    power = models.IntegerField()
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default="WHITE")
    description = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.brand + " " + self.name

class Offer(models.Model):
    offerId = models.AutoField(primary_key=True, default=0)
    available = models.BooleanField()
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    fuel = models.IntegerField(default=100)
    long = models.DecimalField(max_digits=15, decimal_places=13, default=0)
    lat = models.DecimalField(max_digits=15, decimal_places=13, default=0)

    def __str__(self):
        return self.car.brand + " " + self.car.name + " " + str(self.price)