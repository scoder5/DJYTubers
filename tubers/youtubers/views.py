from django.shortcuts import render, get_object_or_404
from .models import Youtuber

# Create your views here.
def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'tubers': tubers,
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id)          #pk=id, Primary Key
    data = {
        'tuber': tuber,
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    #POST request is a request that gets stored into the database
    #GET request is not stored into the database
    tubers = Youtuber.objects.order_by('-created_date')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(name__icontains=keyword)

    data = {
        'tubers': tubers,
    }
    return render(request, 'youtubers/search.html', data)