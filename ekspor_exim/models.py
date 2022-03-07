from django.db import models

# Create your models here.
class Dataekspor(models.Model):
    nopeb = models.CharField(blank=False, max_length=200)
    tanggalpeb = models.DateField(blank=False,)
    npwpeksportir = models.CharField(blank=False, max_length=15)
    eksportir = models.CharField(blank=False, max_length=200)
    penerima = models.CharField(blank=False, max_length=200)
    alamatpenerima = models.CharField(blank=False, max_length=200)
    negarapenerima = models.CharField(blank=False, max_length=200)
    npwpppjk = models.CharField(blank=False, max_length=15)
    ppjk = models.CharField(blank=False, max_length=200)
    carrier = models.CharField(blank=False, max_length=200)
    flight = models.CharField(blank=False, max_length=200)
    pelmuatkode = models.CharField(blank=False, max_length=3)
    pelbongkarkode = models.CharField(blank=False, max_length=3)
    kodevaluta = models.CharField(blank=False, max_length=3)
    devisa = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    jeniskemasan = models.CharField(blank=False, max_length=200)
    jumlahbarang = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    netto = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    bruto = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    noseri = models.CharField(blank=False, max_length=200)
    kodehs = models.CharField(blank=False, max_length=8)
    namabarang = models.CharField(blank=False, max_length=200)
    jumlahitem = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    jeniskemasan = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    nettoitem = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    brutoitem = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    tglberangkat = models.DateField(blank=False,)
    jumlahkoli = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    tonase = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    devisaitem = models.DecimalField(blank=False, max_digits=20, decimal_places=2)
    tarifbk = models.CharField(blank=False, max_length=3)
    bk = models.DecimalField(blank=False, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.nopeb