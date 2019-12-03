from django.db import models
from django.utils import timezone

# Create your models here.
class Carrera(models.Model):
    name = models.CharField(max_length=254, null=False)
    periodo = models.CharField(max_length=254, null=False)
    codigo = models.CharField(max_length=254, null=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'carrera'