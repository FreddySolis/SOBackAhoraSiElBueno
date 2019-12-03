from django.db import models
from django.utils import timezone
from carrera.models import Carrera

# Create your models here.
class Registro(models.Model):
    name = models.CharField(max_length=254, null=False)
    lastname = models.CharField(max_length=254, null=False)
    age = models.CharField(max_length=254, null=False)
    gender = models.CharField(max_length=254, null=False)
    address = models.CharField(max_length=254, null=False)
    carrera = models.ForeignKey(
        Carrera, 
        related_name='career', 
        on_delete = models.CASCADE)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'registro'