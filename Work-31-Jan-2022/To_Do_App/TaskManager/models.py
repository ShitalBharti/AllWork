from django.db import models

# Create your models here.
class Tasks(models.Model):
    Id = models.AutoField(primary_key=True, default=1)
    TaskName = models.CharField(max_length=100)
    TaskDescription = models.CharField(max_length=400)
