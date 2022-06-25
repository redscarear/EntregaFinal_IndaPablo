from cProfile import label
from django.db import models
from django.contrib.auth.models import User
class Evento(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    code = models.IntegerField()
    description = models.TextField(blank = True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='evento_posts')
    def __str__(self):
        return f'{self.name} evento --'