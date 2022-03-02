from django.db import models

class DataImpor(models.Model):
    Nomor_PIB = models.CharField(blank=False, max_length=6)
    Tgl_PIB = models.DateField(blank=False)
    Nm_Importir = models.CharField(max_length=50)


# Create your models here.
