from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def catapp(request):
    template = loader.get_template('templates/base.html')
    return HttpResponse(template.render())