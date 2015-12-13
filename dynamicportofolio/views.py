from django.shortcuts import render
from .models import Portofolio

def portofolio_list(request):
    portofolio = Portofolio.objects.all()
    return render(request, 'dynamicportofolio/portofolio_list.html', {'portofolio':portofolio})
