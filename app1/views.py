from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
# Create your views here.
#def super(request):
    #return HttpResponse("welcometoall")
#def good(request):
    #return HttpResponse("hbehappy")#reate your views here.
def joker(request):
    template="index.html"
    a="i am aparna"
    context={"p":a,"q":"hello all i came directly","n":123456}
    return render(request,template,context)
def tommy(request):
    template="super.html"
    b="my name is aparna"
    context={"k":b,"l":"hello all i hope your doing good","m":567893}
    return render(request,"super.html",context)
def super(request):
    c=[1,2,3,4,5]
    return render(request,"main.html",{"d":c})
def world(request):
    template="reg.html"
    return render(request,"reg.html")
def fly(request):
    template="home.html"
    return render(request,"home.html")
def flower(request):
    return render(request,"flower.html")
def plant(request):
    return render(request,"plant.html")
def root(request):
    name=request.GET.get('name')
    num1=int(request.GET.get('number1'))
    num2=int(request.GET.get('number2'))
    print(name)
    print(num1)
    print(num2)
    sum=num1+num2
    return render(request,"root.html",{'sum':sum,"n":name})
def Postf(request):
     b=PostForm()
     if request.method=="POST":
        b=PostForm(request.POST,request.FILES)
        if b.is_valid():
            b.save()
            return redirect("root")
        else:
            return redirect("plan")
     else:
        b=PostForm()
     return render(request,"Posts.html",{"b":b})
