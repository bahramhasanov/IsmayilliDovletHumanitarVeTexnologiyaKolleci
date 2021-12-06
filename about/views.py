from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView

from about.models import News
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


def fetch_news(request):

    context = {
        'title': 'Fetch Xəbərlər kollec',
    }
    return render(request, 'fetch.html', context=context)
