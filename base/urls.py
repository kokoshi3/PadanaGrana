from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('zamow/', views.zamow, name="zamow"),
    path('login/', views.login, name="login"),
    path('panelPracownika/', views.panelPracownika, name="panelPracownika"),
    path('panelKlienta/', views.panelKlienta, name="panelKlienta"),
]