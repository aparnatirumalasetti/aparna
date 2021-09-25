from django.shortcuts import render,redirect
from .forms import supermarket
#from .models import supermarketsale
from django.contrib.auth.models import  User,auth
from django.contrib import messages

def market(request):
    form=supermarket()
    name=None
    email=None
    price=None
    total_price=0
    food_menu=0
    quantity=0
    profile_pic=None
    if request.method=='POST':
        form=supermarket(request.POST,request.FILES)
        if form.is_valid():
           email=form.cleaned_data.get('email')
           name=form.cleaned_data.get("name")
           quantity=form.cleaned_data.get("quantity")
           food_menu=form.cleaned_data.get("food_menu")
           price=form.cleaned_data.get("price")
           total_price=quantity * price
           profile_pic=form.cleaned_data.get('profile_pic')
           data=supermarketsale.objects.create(customername=name,totalprice=total_price,profile_pic=profile_pic)
           data.save()
           print(total_price)
           print(email)
           print(name)

    return render(request,"market.html",{"form":form,"name":name,"t":total_price,'f':food_menu,'q':quantity,"profile_pic":profile_pic})
# Create your views here.
def registration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        if password==confirm_password:
              if User.objects.filter(username=username).exists():
                  messages.info(request,"username exist")
                  return redirect('reg')
              elif User.objects.filter(email=email).exists():
                 messages.info(request,'email exit')
                 return redirect('reg')
              else:
                reg_data=User.objects.create(username=username,email=email,first_name=firstname,last_name=lastname,password=password)


                reg_data.save()

        else:
            messages.info(request,"password dont match")
    return render(request,'registration.html')
def login(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password1')
         user=auth.authenticate(username=username,password=password)
         if user is not None:
              auth.login(request,user)
              return redirect("welcome")
         else:
             messages.info(request,"username password not match")
             return redirect("login")

    return render(request,'login.html')
def logout(request):
   auth.logout(request)
   return redirect("welcome")
def welcome(request):
 return render(request,'welcome.html')
