from django.shortcuts import render
from django.views.generic import ListView, DetailView

from about.models import Category, News
# Create your views here.


class SingleNews(DetailView):
    model = News
    template_name = 'single-news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = self.object
        context['title'] = self.object.title
        return context


class AllNews(ListView):
    model = News
    template_name = 'all-news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = 'All News'
        return context


def contact(request):

    context = {
        'title': 'Əlaqə',
    }
    return render(request, 'contact.html', context=context)


def about(request):

    context = {
        'title': 'Haqqımızda',
    }
    return render(request, 'about.html', context=context)
