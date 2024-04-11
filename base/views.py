from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home page do zrobienia")

def dostawa(request):
    return HttpResponse("strona dostawy do zrobienia")

def login(request):
    return render(request,'login.html')

def panel(request):
    return HttpResponse("Panel zamowien do zrobienia")