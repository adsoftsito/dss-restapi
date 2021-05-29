from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Estado(models.Model):
    idestado = models.IntegerField()
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.estado

class Municipio(models.Model):
    idmunicipio = models.IntegerField()
    identidad = models.IntegerField()
    nombremunicipio = models.CharField(max_length=200)

    def __str__(self):
        return self.nombremunicipio

class Categoria(models.Model):
    tipo = models.IntegerField()
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Empresa(models.Model):
    idempresa = models.IntegerField()
    identidad = models.IntegerField()
    idmunicipio = models.IntegerField()
    codigoactividad = models.IntegerField()
    nombreempresa = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
    codigopostal = models.IntegerField()
    ciudad = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreempresa


