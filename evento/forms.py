from django import forms
from django.contrib.auth.models import User

class EventoForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre del Evento')
    due_date = forms.DateField(label='Fecha de Evento', widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    author = forms.InlineForeignKeyField(User,related_name='evento_posts')

    