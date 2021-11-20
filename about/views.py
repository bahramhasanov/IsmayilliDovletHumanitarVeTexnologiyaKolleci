from django.shortcuts import render
from django.db.models import Q

from about.models import News
# Create your views here.

  
def news(request):
    qs = None
    wrongSearch = None
    
    # qs = New.objects.all()
    qs = News.objects.order_by('created_at')[::-1][0:3]
    if request.GET.get("search_news"):
        qs = News.objects.filter(Q(name__icontains=request.GET.get("search_news")) | Q(
            description__icontains=request.GET.get("search_news")))
        if not qs:
            wrongSearch = "Netice tapilmadi"
        

    context = {
            'title': 'Yeni xəbərlər kollec',
            'news': qs,
            'wrongsearch': wrongSearch,
    }
    return render(request, 'news.html', context=context)

def fetch_news(request):
    qs = News.objects.all()
    context = {
            'title': 'Fetch Xəbərlər kollec',
            'qs' : qs,
    }
    return render(request, 'fetch.html', context=context)