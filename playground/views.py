from django.shortcuts import render
from django.http import HttpResponse 
from django.core.files import File
from .logic import botResponse 
# Create your views here.  request handler
def index(request):
    # txt=open("som.txt","r")
    # testfile=File(txt)
    # contents=testfile.read()
    
    # contents=botResponse()
    contents=botResponse()
    return render(request,"index.html",{"som":contents})

def login(request):
    return render(request,"login.html")

def data(request):
    if request.method=="POST":
        data=request.POST.get('entryField')
        index(request,data)
