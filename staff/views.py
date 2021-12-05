from django.db.models.aggregates import Avg
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, View


from staff.models import Teacher

class Deputies(View):

    def get(self, request):
        context = {
            'title': 'Rehberlik',
        }
        return render(request, 'deputies.html', context=context)


# ************************************ 


# class teacher(ListView):
#     model = Teacher
#     template_name = 'teacher.html'

#     def get(self, request, *args, **kwargs):
#         # qs = None
#         qs_productversion_all = Teacher.objects.all()

#         # if request.GET.get("search_name"):
#         #     qs = Teacher.objects.filter(Q(name__icontains=request.GET.get("search_name")) | Q(
#         #         surname__icontains=request.GET.get("search_name")))
#         context = {
#             'title': 'Teacher kollec',
#             # 'teacher': qs,
#             'teacher': qs_productversion_all,
#         }
#         return render(request, 'teacher.html', context=context)
    
    
    
    
def teacher(request):
    qs = None
    wrongSearch = None
    
    qs = Teacher.objects.all()

    if request.GET.get("search_name"):
        qs = Teacher.objects.filter(Q(name__icontains=request.GET.get("search_name")) | Q(
            surname__icontains=request.GET.get("search_name")))
        if not qs:
            wrongSearch = "Netice tapilmadi"
        

    context = {
            'title': 'Teacher kollec',
            'teacher': qs,
            'wrongsearch': wrongSearch,
            # 'teacher': teachers,
    }
    return render(request, 'teacher.html', context=context)