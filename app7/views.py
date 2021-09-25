from django.shortcuts import render
def eformget(request,b):
     b=Edubridge.objects.get(id=b)
     return render(request,"eformpra.html",{"b":b})
# Create your views here.
