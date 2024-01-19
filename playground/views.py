from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from .logic import botResponse
from .forms import PostBot
from chatbot_model import model1


# Create your views here.  request handler
def index(request):
    data = "Bot:  Hey!! I am your Tele-Med KIOSK. Tell me your symptoms and I will do the diagnosis!!\n"
    if request.method == "POST":
        question = request.POST.get("entryField")
        data = request.POST.get("data")
        ans = model1.getAnswer(question)
        data += "\n" + "User: " + question + "\n" + "Bot:  " + ans + "\n"
        print("data:", data)
    return render(request, "index.html", {"formValue": data})


def login(request):
    return render(request, "login.html")


def demo(request):
    return render(request, "demo.html")
