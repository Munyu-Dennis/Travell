from django.db import models

# Create your models here.
class Destinations(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
