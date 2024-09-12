from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to recommendation system")

def about(request):
    return HttpResponse("About page")

def hello(request, first_name):
    return HttpResponse(f"Hello, {first_name}")

def add(request, num1, num2):
    return HttpResponse(f"The total is {num1 + num2}")