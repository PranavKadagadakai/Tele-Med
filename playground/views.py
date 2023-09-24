from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.core.files import File
from .logic import botResponse 
from .forms import PostBot
from chatbot_model import model1

# Create your views here.  request handler
def index(request):
    data=""
    if request.method=="POST":
        question=request.POST.get("entryField")
        data=request.POST.get("data")
        ans=model1.getAnswer(question)
        data += "\n" + "Q) " + question + "\n" + "ans: " + ans+"\n"
        print("data:", data)
    return render(request,"index.html",{"formValue":data})

def login(request):
    return render(request,"login.html")


    
