from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    output = 'Сдесь будет главная страница и ссылки на залы'
    return HttpResponse(output)
