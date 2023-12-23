from django.db import models

# Create your models here.
class updates(models.Model):
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField()
    productimg = models.ImageField(upload_to='pics')


