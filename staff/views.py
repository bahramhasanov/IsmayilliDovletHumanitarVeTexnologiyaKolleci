from django.http import FileResponse, Http404
from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic import ListView, View
from about.models import Gallery
from math import ceil

from staff.models import PDF, LibraryFAQ, Teacher


class Deputies(View):

    def get(self, request):
        context = {
            'title': 'Rehberlik',
        }
        return render(request, 'deputies.html', context=context)


class Director(View):
    def get(self, request):
        context = {
            'title': 'Director',
            'teachers': Teacher.objects.all(),
            'main_teacher_image': ceil(Teacher.objects.count()/2)
        }
        return render(request, 'director.html', context=context)


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Teachers'
        return context


class Departments(View):
    def get(self, request):
        context = {
            'title': 'Şöbələr',
        }
        return render(request, 'departments.html', context=context)


class LibraryListView(ListView):
    model = PDF
    template_name = 'library.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Onlayn Kitabxana'
        return context


class LibraryDetailView(View):
    def get(self, request, pk, status):
        try:
            pdf = PDF.objects.get(pk=pk)
        except PDF.DoesNotExist:
            raise Http404("File does not exist")
        response = FileResponse(open(pdf.file.path, 'rb'))
        if status == 'download':
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(
                pdf.file.name)
        else:
            response['Content-Disposition'] = 'inline; filename="{}"'.format(
                pdf.file.name)
        return response


class Libraryinfo(View):
    def get(self, request):
        context = {
            'title': 'Kitabxana haqqında ümümi məlumat',
            'faqs': LibraryFAQ.objects.all(),
        }
        return render(request, 'libraryinfo.html', context=context)
