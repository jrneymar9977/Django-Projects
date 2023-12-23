from django.db import models

# Create your models here.
class sell(models.Model):
    category = models.CharField(max_length=30)
    productname = models.CharField(max_length=50)
    productdescription = models.TextField()
    productprice = models.IntegerField()
    date = models.DateField()
    start_time= models.TimeField()
    end_time = models.TimeField()
    productimg = models.ImageField(upload_to='pics')
    address = models.TextField()