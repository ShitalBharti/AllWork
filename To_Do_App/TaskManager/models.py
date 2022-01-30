from django.db import models

# Create your models here.
class Tasks(models.Model):
    Id = models.AutoField(primary_key=True)
    TaskName = models.CharField(max_length=100)
    TaskDescription = models.CharField(max_length=400)
