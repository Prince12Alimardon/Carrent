from django.db import models

# Create your models here.

TYPE = (
    (0, 'Mechanic'),
    (1, 'Auto'),
    (2, 'AI')
)

class Car(models.Model):
    img = models.ImageField(upload_to='cars')
    name= models.CharField(max_length=212)
    stars = models.IntegerField(default=0)
    price = models.PositiveIntegerField()
    doors = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    transmission = models.IntegerField(choices=TYPE, default=1)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Rent(models.Model):
    wyf = models.CharField(max_length=212)
    wyg = models.CharField(max_length=212)
    jurney_d = models.DateField()
    return_d = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car.name
