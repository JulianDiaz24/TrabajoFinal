from django.db import models

from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class Page(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='base/')
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
