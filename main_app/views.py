from django.http.response import HttpResponse
from django.shortcuts import render
from .finches_class import finches

# Create your views here.


def home(request):
    return HttpResponse('<h1>Home</h1>')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})