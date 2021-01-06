from django.db import models

# Create your models here.

class Course(models.Model): #The class that will stand as a class.
    # CRN
    # Level + Section + Course name #SUBJECT OPTION IS REDUNDENT
    # Status
    # Amount of Followers? Could this create the subset of followed classes? Skip if 0?
    pass

class StudentTracker(models.Model): #The model hat will be one student tracking that class.
    # CRN (How the scraper identifies the student)
    # Student Username (How the student (client-side) identifies their CRNS)
    pass