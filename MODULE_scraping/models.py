from django.db import models

class Course(models.Model): #The model that will function as a class
    CRN = models.IntegerField(primary_key=True,default=0)
    subject = models.CharField(max_length=5,default="")
    section = models.CharField(max_length=16,default="")
    course_name = models.CharField(max_length=32,default="")
    status = models.CharField(max_length=7,default="")
    followers = models.IntegerField(default=0)

class StudentTracker(models.Model): #The model that will be one student tracking that class.
    CRNTracker = models.IntegerField()
    user = models.CharField(max_length=32)
    user_number = models.CharField(max_length=10)