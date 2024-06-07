from django.urls import path
from . import views
from .views import product_list
from django.conf import settings
from django.conf.urls.static import static
from .views import add_to_cart, cart_detail, remove_from_cart
from django.urls import path
from .views import process_payment, payment_success

urlpatterns = [
    path('cart/', cart_detail, name='cart_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.home, name="home"),
    path('products/', product_list, name='product-list'),
    path('zamow/', views.zamow, name="zamow"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('panelPracownika/', views.panelPracownika, name="panelPracownika"),
    path('panelAdmina/', views.panelAdmina, name="panelAdmina"),
    path('zamow/', views.zamow, name="zamow"),
    path('rezerwacja/', views.rezerwacja, name="rezerwacja"),
    path('pay/', process_payment, name='process_payment'),
    path('success/<str:transaction_id>/', payment_success, name='payment_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)