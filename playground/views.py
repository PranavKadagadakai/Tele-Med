from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.core.files import File
from .logic import botResponse 
from .forms import PostBot
from chatbot_model import model1

# Create your views here.  request handler
def index(request):
    a=""
    if request.method=="POST":
        val=request.POST.get("entryField")
        a=model1.getAnswer(val)
    return render(request,"index.html",{"formValue":a})

def login(request):
    return render(request,"login.html")


    
