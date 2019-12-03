from django.db import models
from django.utils import timezone

# Create your models here.
class Registro(models.Model):
    name = models.CharField(max_length=254, null=False)
    lastname = models.CharField(max_length=254, null=False)
    age = models.CharField(max_length=254, null=False)
    gender = models.CharField(max_length=254, null=False)
    address = models.CharField(max_length=254, null=False)
    carrera = models.CharField(max_length=254, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'registro'