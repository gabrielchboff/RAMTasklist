from django.shortcuts import render
from core.forms import TasklistForm
from core.models import Tasklist

def index(request):
    context = { }
    return render(request, 'index.html', context)

def tasklist(request):
    instance = Tasklist.objects.all()
    if request.method == 'POST':
        form = TasklistForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TasklistForm()

    print(instance)
    context = {
        'form':form,
        'tasks': instance
    }
    return render(request, 'tasklist.html', context)

def app_download(request):
    context = {}
    return render(request, 'app_dowload.html', context)

