from django.db import models

# Create your models here.
class StudentResultData(models.Model):
    Id = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=100)
    Maths = models.FloatField(max_length=100)
    History = models.FloatField(max_length=100)
    Geography = models.FloatField(max_length=100)
    English = models.FloatField(max_length=100)
    Civics = models.FloatField(max_length=100)
    Economics = models.FloatField(max_length=100)
    Status = models.CharField(max_length=100)
    Chance_Given = models.IntegerField(default=0)