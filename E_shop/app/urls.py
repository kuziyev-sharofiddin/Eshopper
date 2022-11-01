from django.urls import path, include
from . import views
from .views import MailView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    # addtocart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path('contact_page', views.contact_page, name='contact_page'),
    path('checkout/', views.Checkout, name='checkout'),
    # order_page
    path('order/', views.Your_Order, name='order'),
    # Product_page
    path('product/', views.Product_page, name='product'),
    path('product/<str:id>', views.Product_Detail, name='product_detail'),
    # Search
    path('search/', views.Search, name='search'),
    path('', MailView.as_view(), name='mail'),
]
