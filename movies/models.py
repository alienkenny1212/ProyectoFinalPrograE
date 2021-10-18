from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Pelicula(models.Model):
    name = models.CharField(max_length=100)
    poster = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name="peliculas", on_delete=models.CASCADE
    )

class Cine(models.Model):
    name = models.CharField(max_length=100)

class Sala(models.Model):
    name = models.CharField(max_length=100)
    asientos = models.IntegerField()
    cine = models.ForeignKey(
        Cine, related_name="salas", on_delete=models.CASCADE
    )
    pelicula = models.ForeignKey(
        Pelicula, related_name="salapelis", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name