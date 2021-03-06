from django.db.models.query_utils import Q
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.http import HttpResponseRedirect
from django.shortcuts import render
from math import ceil
# Create your views here.

from django.views.generic import ListView

from core.models import MainPage, Mostquestions
from about.models import Event, Gallery, News
from staff.models import PDF, Department


class Base(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomePage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Home")
        context['mostquestions'] = Mostquestions.objects.all()
        context['news'] = News.objects.order_by('-created_at')[:3]
        context['events'] = Event.objects.order_by('-created_at')[:2]
        context['galleries'] = Gallery.objects.all()
        context['main_gallery_image'] = ceil(Gallery.objects.count()/2)
        context['mainpage'] = MainPage.objects.last()
        context['departments'] = Department.objects.all()
        return context


def change_language(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'az' or request.GET.get('lang') == 'ru':
        translation.activate(request.GET.get('lang'))
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('django_language', request.GET['lang'])
        return response


class Search(ListView):
    template_name = "search.html"
    context_object_name = 'news'

    def get(self, request, *args, **kwargs):
        queryset = None
        search_text = self.request.GET.get('search_text')
        if request.GET and search_text:
            queryset = list(News.objects.filter(
                Q(title__icontains=search_text) | Q(description__icontains=search_text)))
            queryset += list(PDF.objects.filter(
                Q(title__icontains=search_text) | Q(category__title__icontains=search_text)))

        context = {
            'title': _('Search'),
            'results': queryset,
            'search_text': search_text,
            'result_count': len(queryset),
        }
        return render(request, 'search.html', context=context)
