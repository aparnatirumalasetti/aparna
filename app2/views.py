from django.shortcuts import render
from django.http import HttpResponse# Create your views here.
def need(request):
    return HttpResponse("tommarow is holyday")
def wow(request):
    return HttpResponse("today class is postponed")# Create your views here.
