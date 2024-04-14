from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'homepage.html')

def zamow(request):
    return render(request,'zamow.html')

def rezerwacja(request):
    return render(request,'rezerwacja.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/panelPracownika')  # zmień '/home' na URL docelowy po zalogowaniu
        else:
            return HttpResponse("Nieprawidłowa nazwa użytkownika lub hasło.")
    return render(request, 'login.html')  # Nazwa twojego pliku HTML dla formularza logowania
    # return render(request,'login.html')

def rejestracja(request):
    return render(request,'rejestracja.html')

def panelPracownika(request):
    return render(request,'panelPracownika.html')

def panelKlienta(request):
    return render(request,'panelKlienta.html')





