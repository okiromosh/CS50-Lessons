from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def brain(request):
    # create a function to a specific route .ie. /hello/brain
    return HttpResponse("Hello, Brain")


def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
