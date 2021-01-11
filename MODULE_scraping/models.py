from django.db import models

# Create your models here.

class Course(models.Model): #The class that will stand as a class.
    # CRN
    # Level + Section + Course name #SUBJECT OPTION IS REDUNDENT
    # Status
    # Amount of Followers? Could this create the subset of followed classes? Skip if 0?
    CRN = models.IntegerField()
    level = models.CharField(max_length=16)
    section = models.CharField(max_length=16)
    course_name = models.CharField(max_length=32)
    status = models.BooleanField(default=False)
    #followers = models.Integerfield()

class StudentTracker(models.Model): #The model hat will be one student tracking that class.
    CRNTracker = models.IntegerField()
    user = models.CharField(max_length=32)
    user_number = models.CharField(max_length=10)