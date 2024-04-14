from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('zamow/', views.zamow, name="zamow"),
    path('login/', views.login_view, name="login"),
    path('rejestracja/', views.rejestracja, name="rejestracja"),
    path('panelPracownika/', views.panelPracownika, name="panelPracownika"),
    path('panelKlienta/', views.panelKlienta, name="panelKlienta"),
    path('zamow/', views.zamow, name="zamow"),
    path('rezerwacja/', views.rezerwacja, name="rezerwacja"),

]
