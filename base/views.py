from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home page do zrobienia")

def zamow(request):
    return HttpResponse("strona zamawiania do zrobienia")

def login(request):
    return render(request,'login.html')

def panelPracownika(request):
    return render(request,'panelPracownika.html')

def panelKlienta(request):
    return render(request,'panelKlienta.html')



