from django.urls import path
from .views import *
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'sub_categories', views.Sub_CategoryViewSet,
                basename='sub_categories')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'contact_uss', views.Contact_usViewSet,
                basename='contact_us')
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'brands', views.BrandViewSet, basename='brands')
urlpatterns = router.urls
