from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'matcher/' )


def info(request):
    return HttpResponse('<h1>Info Here</h1>')

