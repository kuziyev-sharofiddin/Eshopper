from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from app.models import Category,Sub_Category,Product,Contact_us,Order,Brand
from .serializers import CategorySerializer,Sub_CategorySerializer,ProductSerializer,Contact_usSerializer,OrderSerializer,BrandSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class CategoryList(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class Sub_CategoryList(ListCreateAPIView):
    queryset=Sub_Category.objects.all()
    serializer_class=Sub_CategorySerializer

class Sub_CategoryDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Sub_Category.objects.all()
    serializer_class=Sub_CategorySerializer

class ProductList(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class Contact_usList(ListCreateAPIView):
    queryset=Contact_us.objects.all()
    serializer_class=Contact_usSerializer

class Contact_usDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Contact_us.objects.all()
    serializer_class=Contact_usSerializer

class OrderList(ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class BrandList(ListCreateAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer

class BrandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer

