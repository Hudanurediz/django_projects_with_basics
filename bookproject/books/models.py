from django.db import models
from django.http import HttpResponse
# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    USERNAME_FIELD = 'email'


class Author(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField('created')

class Book(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField('created')
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=3, max_digits=6,null=True)
    release_date=models.DateField(max_length=4,null=True)

