from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Cat
# Create your views here.

def catapp(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def review(request):
    template = loader.get_template('review.html')
    return HttpResponse(template.render())





