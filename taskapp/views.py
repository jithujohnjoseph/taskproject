

from django.http import HttpResponse
from django.shortcuts import render
from . models import place


# Create your views here.

def home(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x*y
#     res3=x/y
#     return render(request,"result.html",{'add':res,'sub':res1,'mul':res2,'div':res3})