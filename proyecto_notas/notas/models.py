from django.db import models

class Nota(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Titulo: {self.titulo} - Descripcion {self.descripcion}'