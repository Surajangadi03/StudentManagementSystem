from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES=[
        ('male','Male'),
        ('female','Female')
    ]
    ID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Email = models.EmailField()
    ContactNumber = models.IntegerField()
    

