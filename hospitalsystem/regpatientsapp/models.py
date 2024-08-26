from django.db import models

# Create your models here.

class Patients(models.Model):
    #patientid = models.AutoField()
    names = models.CharField(max_length=25)
    gender = models.CharField(max_length=9)
    age = models.IntegerField()
    patientssituation = models.TextField()
    healthissues = models.CharField(max_length=10)
    dateregistered = models.DateField()

    def __str__(self):
        return self.names






















































