from django.db import models

# Create your models here.
# ORM : Database Object relational Mapping

class Categoria(models.Model):
	nombre_cat = models.CharField(max_length=100)
	desc = models.TextField()


class Producto(models.Model):
	nombre = models.CharField(max_length=200)
	stock = models.IntegerField()
	precio = models.IntegerField()
	categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

