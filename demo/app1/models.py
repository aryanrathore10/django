from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    email= models.EmailField()
    adddress=models.TextField()
    ID= models.AutoField()
    
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.TextField()
    id= models.AutoField()
    
