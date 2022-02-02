from django.db import models

# Create your models here.
class Tasks(models.Model):
    Id = models.AutoField(primary_key=True)
    TaskName = models.CharField(max_length=100)
    TaskDescription = models.CharField(max_length=400)

class Signup(models.Model):
    Username = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    Confirm_Password = models.CharField(max_length=100)