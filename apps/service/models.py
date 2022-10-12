from django.db import models


# Create your models here.

class Service(models.Model):
    icon = models.ImageField(upload_to='Service')
    title = models.CharField(max_length=212)
    content = models.TextField()

    def __str__(self):
        return self.title
