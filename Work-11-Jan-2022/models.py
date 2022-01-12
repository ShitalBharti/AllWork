from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(null = False,default=1)
    ename = models.CharField("Employee name", max_length=20, blank = False, null = False)
    sal = models.IntegerField(null = False,default=1)

    def __str__(self):
        return self.ename