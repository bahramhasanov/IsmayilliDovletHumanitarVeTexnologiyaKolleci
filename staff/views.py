from http.client import HTTPResponse
import os
from django.http import FileResponse, Http404
from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic import ListView, View
from django.utils.translation import ugettext_lazy as _
from math import ceil

from staff.models import PDF, Deputy, HeadOfDepartment, Library, LibraryFAQ, Teacher, Director


class DeputiesView(View):

    def get(self, request):
        context = {
            'title': _('Rəhbərlik'),
            'deputies': Deputy.objects.all()
        }
        return render(request, 'deputies.html', context=context)


class DirectorView(View):
    def get(self, request):
        context = {
            'title': _('Director'),
            'teachers': Teacher.objects.all(),
            'main_teacher_image': ceil(Teacher.objects.count()/2),
            'director': Director.objects.last(),
        }
        return render(request, 'director.html', context=context)


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Teachers')
        return context


class DepartmentsView(ListView):
    model = HeadOfDepartment
    template_name = 'departments.html'
    context_object_name = 'headofdepartment'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Departments')
        return context


class LibraryListView(ListView):
    model = PDF
    template_name = 'library.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Onlayn Kitabxana')
        return context


class LibraryDetailView(View):
    def get(self, request, slug, status):
        try:
            pdf = PDF.objects.get(slug=slug)
        except PDF.DoesNotExist:
            raise Http404("File does not exist")
        response = FileResponse(open(pdf.file.path, 'rb'))
        if status == 'download':
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(
                pdf.file.name)
        else:
            # filepath = os.path.join('media', pdf.file.name)
            # return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
            # image_data = open(pdf, "rb").read()
            # return HTTPResponse(image_data, contenttype='application/pdf')
            # print('pdf.file.path')
            response['Content-Disposition'] = 'inline; filename="{}"'.format(
                pdf.file.name)
        return response


class LibraryInfoView(View):
    def get(self, request):
        context = {
            'title': _('Kitabxana haqqında ümümi məlumat'),
            'faqs': LibraryFAQ.objects.all(),
            'library' : Library.objects.last()
        }
        return render(request, 'libraryinfo.html', context=context)
