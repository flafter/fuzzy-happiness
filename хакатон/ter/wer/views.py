from django.shortcuts import render
from .models import *
# Create your views here.
def blog(request):
    revizs = Reviz.objects.all()
    if request.method =="POST": 
        retr =request.POST.get("name")
        ter =request.POST.get("text")
        Reviz.objects.create(name =retr,text =ter)    
    return render(request, "odzov.html",{"reviz":revizs})
def ter(request):   
    return render(request, "moo.html")
def wer(request):
    prodkts = Prodkt.objects.all() 
    return render(request, "slider.html",{"prodkt":prodkts})
