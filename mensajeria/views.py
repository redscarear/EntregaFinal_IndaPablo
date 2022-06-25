from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from mensajeria.models import Mensajeria
from django.contrib.auth.models import User

class MensajeriaListView(ListView):
    model = Mensajeria
    template_name = "mensajeria/mensajeria_list.html"


class MensajeriaDetailView(DetailView):
    model = Mensajeria
    template_name = "mensajeria/mensajeria_detail.html"
    fields = ['title', 'emisor', 'receptor', 'content', 'slug']

class MensajeriaEnviadosView(ListView):
    model = Mensajeria
    template_name = "mensajeria/mensajeria_enviados.html"
    

class MensajeriaRecibidosView(ListView):
    model = Mensajeria
    template_name = "mensajeria/mensajeria_recibidos.html"
    


class MensajeriaCreateView(LoginRequiredMixin, CreateView):
    model = Mensajeria
    success_url = reverse_lazy('mensajeria:mensajeria-list')
    fields = ['title', 'emisor', 'receptor', 'content', 'slug']


class MensajeriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Mensajeria
    success_url = reverse_lazy('mensajeria:mensajeria-list')
    fields = ['title', 'emisor', 'receptor', 'content', 'slug']


class MensajeriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Mensajeria
    success_url = reverse_lazy('mensajeria:mensajeria-list')

		
