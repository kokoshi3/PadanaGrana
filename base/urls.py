from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dostawa/', views.dostawa, name="dostawa"),
    path('login/', views.login, name="login"),
    path('panel', views.panel, name="panel"),
]