from django.db import models


# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name
