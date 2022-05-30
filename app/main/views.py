from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('about')


def index1(request):
    return HttpResponse('Биринчи бет')


def index2(request):
    return HttpResponse('Экинчи бет')


def index3(request):
    return HttpResponse('Учунчу<br/> бет')


def index4(request):
    return HttpResponse('Тортунчу бет')


def index5(request):
    return HttpResponse('Бешинчи бет')
