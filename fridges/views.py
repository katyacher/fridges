from django.shortcuts import render
from django.http import  HttpResponse
from django.template import loader, Context
from .models import fridges

def table(request):
    posts = fridges.objects.all()
    t = loader.get_template("table.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c)) 
# Create your views here.
