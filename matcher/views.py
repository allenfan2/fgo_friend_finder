from django.shortcuts import render
# Create your views here.


data = [
    {'name': 'Bob'},
    {'name': 'Jack'}
]


def home(request):
    context = {
        'peoples': data
    }
    return render(request, 'matcher/home.html', context)


def info(request):
    return render(request, 'matcher/info.html', {'title': 'Info'})

