from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from base.models import Product, Cart, CartItem


# Create your views here.

def home(request):
    return render(request, 'homepage.html')


def zamow(request):
    return render(request, 'zamow.html')


def rezerwacja(request):
    return render(request, 'rezerwacja.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/panelAdmina')  # zmień '/home' na URL docelowy po zalogowaniu
        elif user is not None and user.is_staff:
            login(request, user)
            return redirect('/panelPracownika')
        else:
            return HttpResponse("Nieprawidłowa nazwa użytkownika lub hasło.")
    return render(request, 'login.html')  # Nazwa twojego pliku HTML dla formularza logowania
    # return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def panelPracownika(request):
    return render(request, 'panelPracownika.html')


@login_required
def panelAdmina(request):
    return render(request, 'panelAdmina.html')

def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'product_list.html', {'products': products})

def get_cart(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id:
        cart, created = Cart.objects.get_or_create(id=cart_id)
        if not created:
            return cart
        return Cart.objects.create()

def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    request.session['cart_id'] = cart.pk
    return redirect('cart_detail')

def cart_detail(request):
    cart = get_cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart_detail')

def checkout(request):
    # Logika dla widoku checkout
    return render(request, 'checkout.html')