from django.shortcuts import render

def index(request):
    context = { }
    return render(request, 'index.html', context)

def tasklist(request):
    context = {}
    return render(request, 'tasklist.html', context)

def app_download(request):
    context = {}
    return render(request, 'app_dowload.html', context)

