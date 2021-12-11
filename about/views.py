from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from about.models import Category, News, Specialty, Faculty
# Create your views here.


class SingleNews(DetailView):
    model = News
    template_name = 'single-news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = self.object
        context['title'] = self.object.title
        context['related_news'] = News.objects.filter(category=self.object.category).exclude(id=self.object.id)[0:4]
        return context


class AllNews(ListView):
    model = News
    template_name = 'all-news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = 'Bütün xəbərlər'
        return context



class Contact(View):
    
    def get(self, request):
        context = {
           'title': 'Əlaqə',
        }
        return render(request, 'contact.html', context=context)


class About(View):
    
    def get(self, request):
        context = {
           'title': 'Haqqımızda',
        }
        return render(request, 'about.html', context=context)


class FBK(View):
    
    def get(self, request):
        context = {
           'title': 'FBK',
        }
        return render(request, 'FBK.html', context=context)
    
    
# **********************************


class AllFaculty(ListView):
    model = Faculty
    template_name = 'faculties.html'
    context_object_name = 'faculties'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faculities'] = Faculty.objects.all()
        context['title'] = 'fbklar'
        return context

class SingleFaculty(DetailView):
    model = Faculty
    template_name = 'single-faculty.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faculty'] = self.object
        context['title'] = self.object.title
        return context
    
class AllSpeciality(ListView):
    model = Specialty
    template_name = 'specialties.html'
    context_object_name = 'specialties'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.all()
        context['title'] = 'Ixtisaslar'
        return context
    

class SingleSpeciality(DetailView):
    model = Specialty
    template_name = 'single-specialty.html'
    context_object_name = 'specialty'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialty'] = self.object
        context['title'] = self.object.title
        return context