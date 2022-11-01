from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Product, Contact_us, Order, Brand, Mail, Tip
from django.contrib.auth import authenticate, login
from app.models import UserCreateForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import MailForm

# Create your views here.


def home(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    nam = Tip.objects.all()
    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(
            category_sub=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()
    return render(request, 'home.html', {'category': category, 'product': product, 'brand': brand, 'nam': nam})


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreateForm()
        return render(request, 'registration/signup.html', {
            'form': form
        })


@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def contact_page(request):
    if request.method == 'POST':
        contact = Contact_us(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        contact.save()

    return render(request, 'contact.html', {})


def Checkout(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)

        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a*b
            order = Order(
                user=user,
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                address=address,
                phone=phone,
                pincode=pincode,
                total=total,
            )
            order.save()
        request.session['cart'] = {}
        return redirect('home')

    return HttpResponse('This is Checkout page')


def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = Order.objects.filter(user=user)
    return render(request, 'order.html', {'order': order})


def Product_page(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    categoryID = request.GET.get('category')
    brandID = request.GET.get('brand')
    if categoryID:
        product = Product.objects.filter(
            category_sub=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()
    return render(request, 'product.html', {'category': category, 'product': product, 'brand': brand})


def Product_Detail(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request, 'product_detail.html', {'product': product})


def Search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'product': product})


class MailView(CreateView):
    form_class = MailForm
    model = Mail
