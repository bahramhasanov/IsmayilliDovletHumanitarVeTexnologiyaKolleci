from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils import translation
from django.http import HttpResponseRedirect

# Create your views here.


class Base(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def change_language(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'az' or request.GET.get('lang') == 'ru':
        translation.activate(request.GET.get('lang'))
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('django_language', request.GET['lang'])
        return response
