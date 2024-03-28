from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files import File
from TeleMed_model import model1


# Create your views here.  request handler
def index(request):
    data = "Bot:  Hey!! I am your Tele-Med KIOSK. Tell me your symptoms and I will do the diagnosis!!\n"
    if request.method == "POST":
        question = request.POST.get("entryField")
        data_received = request.POST.get("data")
        ans = model1.getAnswer(question)

        if isinstance(ans, dict) and len(ans) == 3:
            data += "\n" + "User: " + question + "\n" + "Bot:"
            for key, value in ans.items():
                data += "\n" + f"{key}: {value}"
        else:
            # Convert ans to a string before appending to data
            data += "\n" + "User: " + question + "\n" + "Bot: " + str(ans[0]['answer'])

        print("data:", data)

    return render(request, "index.html", {"formValue": data})


def login(request):
    return render(request, "login.html")


def demo(request):
    return render(request, "demo.html")
