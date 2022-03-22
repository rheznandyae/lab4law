from django.db import models
from django.forms import CharField

# Create your models here.
class Mahasiswa(models.Model):
    nama = models.CharField(max_length=50, null=True, blank=True)
    alamat = models.CharField(max_length=100, null=True, blank=True)
    npm = models.CharField(max_length=10, primary_key=True)
    photo = models.FileField(null=True, upload_to='mahasiswa/media/images')