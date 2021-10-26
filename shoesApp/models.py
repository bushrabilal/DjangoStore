from django.db import models

# Create your models here.


class Shoes(models.Model):
    name = models.CharField(max_length=75)
    brand = models.CharField(max_length=75)
    img= models.ImageField(upload_to='pics')
    price =  models.IntegerField()
    sale_price = models.IntegerField()
    sale_active = models.BooleanField(default=False)
    rating = models.IntegerField()