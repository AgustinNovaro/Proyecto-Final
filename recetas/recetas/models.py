from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    sabor = models.CharField(max_length=50)
    ingredientes = models.TextField(max_length=30)
    instrucciones = models.TextField(max_length=30)
    tiempo_preparacion = models.IntegerField()
    dificultad = models.CharField(max_length=20)
    num_porciones = models.IntegerField()
    # imagen = models.ImageField(upload_to='recetas/')  # Ajusta la ruta según tu configuración

    def __str__(self):
        return self.nombre

