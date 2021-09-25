from django.shortcuts import render,redirect
from .models import Edubridge
from .forms import EdubridgeForm
from django.contrib import messages
from  django.db.models import Q

def eform(request):
    form=EdubridgeForm()
    if request.method=='POST':
        form=EdubridgeForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
           return redirect("eall")

           return redirect("hello")
    else:
         form=EdubridgeForm()
    return render(request,"eform.html",{"form":form})

def eall(request):
    data=Edubridge.objects.all()
    query=request.GET.get('s')
    print(query)
    if query is not None:
        data=data.filter(Q(learners_name__icontains=query)|
                 Q(adress__icontains=query))
        messages.info(request,"YOUR INFORMATION BASED ON YOUR INPUT")

    return render(request,"eall.html",{"data":data})
    #data=data.filter(Q(learners_name__icontains=query) |
              # Q(adress__icontains=query)
               #)




def hello(request):
    return render(request,"query.html")# Create your views here.
def eformget(request,a):
     a=Edubridge.objects.get(id=a)
     return render(request,"eformget.html",{"a":a})
def eformupdate(request,a):
    a=Edubridge.objects.get(id=a)
    form=EdubridgeForm()
    if request.method=='POST':
        form=EdubridgeForm(request.POST,request.FILES,instance=a)
        if form.is_valid():
           form.save()
           return redirect("eall")
        else:
           return redirect("hello")
    else:
         form=EdubridgeForm()
    return render(request,'eformupdate.html',{'form':form,'a':a})
def eformdelete(request,t):
        a=Edubridge.objects.get(id=t)
        a.delete()
        return redirect('eall')
