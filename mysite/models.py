from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    farmsize=models.CharField(max_length=100)
    message=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
    
