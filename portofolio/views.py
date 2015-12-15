from django.shortcuts import render
from .models import Porto

def index(request):
    portofolio = Porto.objects.all()
    context_dict = {'portofolio':portofolio}
    return render (request, 'portofolio/index.html', context_dict)

def portofolio_list(request):
    portofolio = Portofolio.objects.all()
    return render(request, 'portofolio/index.html',{'portofolio':portofolio})
