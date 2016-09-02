from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Schedule
from django.shortcuts import redirect
from .forms import ScheduleForm

def post_list(request):
    posts = Schedule.objects.all()
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = ScheduleForm()
    return render(request, 'todo/list.html', {'posts': posts, 'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Schedule, pk=pk)
    post.delete()
    return redirect('todo.views.post_list')
