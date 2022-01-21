from django.db import models

# Create your models here.
'''
Models are use to define database tables.
Models is having Model field references
makemigrations - use to save changes done in models.py file into migrations folder
makemigrate - apply the save changes in database table created by makemigrations
'''
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

