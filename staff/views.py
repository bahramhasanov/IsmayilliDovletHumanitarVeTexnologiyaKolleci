from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic import ListView, View


from staff.models import Teacher


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
        }
        return render(request, 'director.html', context=context)


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Teachers'
        return context
