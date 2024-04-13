from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return render(request,'homepage.html')

def zamow(request):
    return render(request,'zamow.html')

def rezerwacja(request):
    return render(request,'rezerwacja.html')

def login(request):
    return render(request,'login.html')

def rejestracja(request):
    return render(request,'rejestracja.html')

def panelPracownika(request):
    return render(request,'panelPracownika.html')

def panelKlienta(request):
    return render(request,'panelKlienta.html')





