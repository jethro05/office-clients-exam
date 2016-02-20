from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from clients.models import Client, Contact

class ClientListView(ListView):
    model = Client

    def get_context_data(self, **kwargs):
         context = super(ClientListView, self).get_context_data(**kwargs)
         return context


class ClientDetailView(DetailView):
    model = Client

    def get_context_data(self, **kwargs):
         context = super(ClientDetailView, self).get_context_data(**kwargs)
         return context


class ContactDetailView(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
         context = super(ContactDetailView, self).get_context_data(**kwargs)
         return context


