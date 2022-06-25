from django import forms
from django.contrib.auth.models import User



class MensajeriaForm(forms.Form):
    title = forms.CharField(max_length=200, unique=True)
    slug = forms.SlugField(max_length=500, unique=True)
    emisor = forms.InlineForeignKeyField(User,related_name='emisor')
    receptor = forms.InlineForeignKeyField(User,related_name='receptor')
    updated_on = forms.DateTimeField(auto_now= True)
    content = forms.Textarea()
    created_on = forms.DateTimeField(auto_now_add=True)
    
