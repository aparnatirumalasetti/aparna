from django.shortcuts import render
from django.http import HttpResponse# Create your views here.
def fine(request):
    return HttpResponse("dont depends on others")
def nice(request):
    return HttpResponse("try to do it alone")# Create your views here.




# Create your views here.
