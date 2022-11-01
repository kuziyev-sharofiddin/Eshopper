from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import Category, Sub_Category, Product, Contact_us, Order, Brand
from .serializers import CategorySerializer, Sub_CategorySerializer, ProductSerializer, Contact_usSerializer, OrderSerializer, BrandSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Sub_CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Contact_usViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Contact_us.objects.all()
    serializer_class = Contact_usSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
