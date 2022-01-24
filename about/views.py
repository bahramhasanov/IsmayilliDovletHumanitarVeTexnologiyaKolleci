from datetime import datetime
from about.models import CareerSupport, Category, Event, Gallery, News, Practic, Specialty, Faculty, Admissionrules, About, Dateofcreate
from core.models import Mostquestions
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

# Create your views here.
from django.utils.translation import ugettext_lazy as _


class SingleNews(DetailView):
    model = News
    template_name = 'single-news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = self.object
        context['title'] = self.object.title
        context['related_news'] = News.objects.filter(
            category=self.object.category).exclude(id=self.object.id)[0:4]
        return context


class AllNews(ListView):
    model = News
    template_name = 'all-news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = _('Bütün xəbərlər')
        return context


class Contact(View):

    def get(self, request):
        context = {
            'title': _('Əlaqə',)
        }
        return render(request, 'contact.html', context=context)


class FBK(View):

    def get(self, request):
        context = {
            'title': _('FBK'),
        }
        return render(request, 'FBK.html', context=context)


class AllFaculty(ListView):
    model = Faculty
    template_name = 'faculties.html'
    context_object_name = 'faculties'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faculities'] = Faculty.objects.all().order_by('updated_at')
        context['title'] = 'FBKlar'
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
        context['title'] = _('Ixtisaslar')
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


class Totaladmissionrules(ListView):
    model = Admissionrules
    template_name = 'totaladmissionrules.html'
    context_object_name = 'totaladmissionrules'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['totaladmissionrules'] = Admissionrules.objects.all()
        context['title'] = _('Ümumi qəbul qaydaları')
        return context


class From9admissionrules(ListView):
    model = Admissionrules
    template_name = 'from9admissionrules.html'
    context_object_name = '9_admissionrules'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['totaladmissionrules'] = Admissionrules.objects.all()
        context['title'] = _('9-cu sinifdən qəbul qaydaları')
        return context


class From11admissionrules(ListView):
    model = Admissionrules
    template_name = 'from11admissionrules.html'
    context_object_name = '11_admissionrules'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['totaladmissionrules'] = Admissionrules.objects.all()
        context['title'] = _('11-cu sinifdən qəbul qaydaları')
        return context


class AboutView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'abouts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['title'] = _('Haqqımızda')
        return context


class DateofcreateView(ListView):
    model = Dateofcreate
    template_name = 'dateofcreate.html'
    context_object_name = 'dateofcreates'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dateofcreates'] = Dateofcreate.objects.all()
        context['title'] = _('Yaradılma tarixi')
        return context


class EventsView(ListView):
    model = Event
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['future_events'] = Event.objects.filter(
            date__gte=datetime.now())
        context['recent_events'] = Event.objects.filter(
            date__lte=datetime.now())
        context['title'] = _('Tədbirlər')
        return context


class AllPractic(ListView):
    model = Practic
    template_name = 'practies.html'
    context_object_name = 'practies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['practies'] = Practic.objects.all()
        context['title'] = _('Təcrübə Adları')
        return context


class SinglePractic(DetailView):
    model = Practic
    template_name = 'single-practic.html'
    context_object_name = 'practic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['practic'] = self.object
        context['title'] = self.object.title
        return context


class GalleryView(ListView):
    model = Gallery
    template_name = 'galleries.html'
    context_object_name = 'practies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['galleries'] = Gallery.objects.all()
        context['title'] = _('Qalereya')
        return context


class FAQView(ListView):
    model = Mostquestions
    template_name = "FAQ.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faq'] = Mostquestions.objects.all()
        context['title'] = _('FAQ')
        return context


class CareerSupportView(ListView):
    model = CareerSupport
    template_name = 'careersupport.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['careersupports'] = CareerSupport.objects.all()
        return context
