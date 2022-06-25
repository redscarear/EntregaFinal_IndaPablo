from django.db import models
from django.contrib.auth.models import User
class Productor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    cuil = models.IntegerField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='productor_posts')
    email = models.EmailField()
    def __str__(self):
        return f'Nombre del Productor: {self.name} {self.last_name} -- '