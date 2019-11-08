from django.db import models

# Create your models here.
class AllDestinations(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    hoteltype = models.CharField(max_length=255)
    inclusive = models.BooleanField(default=False)
    



