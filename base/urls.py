from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', product_list, name='product-list'),
    path('zamow/', views.zamow, name="zamow"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('panelPracownika/', views.panelPracownika, name="panelPracownika"),
    path('panelAdmina/', views.panelAdmina, name="panelAdmina"),
    path('zamow/', views.zamow, name="zamow"),
    path('rezerwacja/', views.rezerwacja, name="rezerwacja"),


]
