from django.db import models

# Create your models here.

class menu(models.Model):
    entrada = models.CharField('Entrada', max_length = 60, default ='', blank = True)
    fondo = models.CharField('Fondo', max_length = 60, default = '', blank = True)
    postre = models.CharField('Postre', max_length = 60, default = '', blank = True)
    hipocal = models.CharField('Hipocalórico', max_length = 60, default = '', blank = True)

    