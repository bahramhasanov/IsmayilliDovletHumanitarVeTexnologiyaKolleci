from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

from django.views.generic import ListView

from core.models import Mostquestions


class Base(TemplateView):
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HomePage(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mostquestions'] = Mostquestions.objects.all()
        return context
    