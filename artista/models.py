from django.db import models
from django.contrib.auth.models import User
class Artista(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    instrument = models.CharField(max_length=40)
    cuil = models.IntegerField()
    email = models.EmailField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='artista_posts')
    def __str__(self):
        return f'Nombre del Artista: {self.name} {self.last_name} -- '