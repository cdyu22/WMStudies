from django.db import models

class Course(models.Model): #The model that will function as a class
    CRNR = models.IntegerField(primary_key=True,default=0)
    subject = models.CharField(max_length=5,default="")
    sectionR = models.CharField(max_length=16,default="")
    course_nameR = models.CharField(max_length=32,default="")
    statusR = models.CharField(max_length=7,default="")
    followersR = models.IntegerField(default=0)

class StudentTracker(models.Model): #The model that will be one student tracking that class.
    CRNTracker = models.IntegerField()
    user = models.CharField(max_length=32)
    user_number = models.CharField(max_length=10)