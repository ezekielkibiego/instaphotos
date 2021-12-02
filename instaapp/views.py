from django.shortcuts import render
from django.http  import HttpResponse


def welcome(request):
    return HttpResponse('Welcome to Instaphotos')

def index(request):
    return render(request, 'all-insta/index.html')