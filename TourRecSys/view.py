from django.http import HttpResponse
from django.shortcuts import render


def init(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'detail.html')

