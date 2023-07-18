from django.db import models
import weekday_field
import datetime

# Create your models here.

    
class Bar(models.Model):
    name = models.CharField(max_length=100, default='BarName')
    address = models.CharField(max_length=200, default = "BarAddress")
    hours = models.CharField(max_length=400, default="BarHours")
    

    def __str__(self):
        return self.name
    

class Special(models.Model):
    name= models.CharField(max_length=100, default="name")
    days= models.CharField(max_length=200)
    details= models.CharField(max_length=500, default="description")
    bar=models.ForeignKey(Bar, on_delete=models.CASCADE, related_name="specials")

    def __str__(self):
        return self.name