from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from offices.models import Office

class OfficeListView(ListView):
    model = Office

    def get_context_data(self, **kwargs):
        context = super(OfficeListView, self).get_context_data(**kwargs)
        return context

class OfficeDetailView(DetailView):
    model = Office

    def get_context_data(self, **kwargs):
        context = super(OfficeDetailView, self).get_context_data(**kwargs)
        return context
