from django.db import models

class Course(models.Model): #The model that will function as a class
    CRN = models.IntegerField()
    level = models.CharField(max_length=16)
    section = models.CharField(max_length=16)
    course_name = models.CharField(max_length=32)
    status = models.BooleanField(default=False)
    followers = models.IntegerField()

class StudentTracker(models.Model): #The model that will be one student tracking that class.
    CRNTracker = models.IntegerField()
    user = models.CharField(max_length=32)
    user_number = models.CharField(max_length=10)