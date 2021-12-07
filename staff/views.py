from django.db.models.aggregates import Avg
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from staff.models import Teacher

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Teachers'
        return context