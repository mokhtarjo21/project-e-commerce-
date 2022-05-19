from pydoc import describe
from zoneinfo import available_timezones
from django.db import models

# Create your models here.
class category(models.Model):
    name =models.CharField(max_length=30)
    description=models.TextField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name =models.CharField(max_length=50)
    content =models.TextField()
    categorid =models.ForeignKey(category,on_delete=models.CASCADE)
    price =models.DecimalField(max_digits=7,decimal_places=2)
    image =models.ImageField(upload_to='photo/%y/%m/%d')
    available =models.BooleanField(default=True)
    date_n =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class cart(models.Model):
    price =models.DecimalField(max_digits=7,decimal_places=0)
    num =models.DecimalField(max_digits=7,decimal_places=0)
    