from django.db import models
class Admin(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
class Book(models.Model): 
    Book_Name=models.CharField(max_length=50)
    isbn=models.CharField(max_length=30)
    Author=models.CharField(max_length=30)
    Language=models.CharField(max_length=20)

