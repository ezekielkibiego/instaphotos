from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images


def welcome(request):
    return HttpResponse('Welcome to Instaphotos')

def index(request):

    image = Images.objects.all().order_by('-id')

    return render(request, 'all-insta/index.html',{'image':image})
   