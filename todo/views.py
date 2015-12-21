from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Schedule
from django.shortcuts import redirect

def post_list(request):
    posts = Schedule.objects.all()
    return render(request, 'todo/list.html', {'posts': posts})

def post_remove(request, pk):
    post = get_object_or_404(Schedule, pk=pk)
    post.delete()
    return redirect('todo.views.post_list')
