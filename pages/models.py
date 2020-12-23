from django.db import models

# Create your models here.
class TestModel(models.Model):
    title = models.CharField
    description = models.TextField

class Person(models.Model):
    first_name = models.CharField(max_length=30,blank=False)
    last_name = models.CharField(max_length=30,blank=False)