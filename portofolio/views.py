from django.shortcuts import render
from .models import Portofolio


def index(request):
    context_dict = {}
    return render (request, 'portofolio/index.html', context_dict)

def portofolio_list(request):
    portofolio = Portofolio.objects.all()
    return render(request, 'portofolio/index.html',{'portofolio':portofolio})
