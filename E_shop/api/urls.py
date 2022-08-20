from django.urls import path
from .views import *

urlpatterns=[
    path('v1/<int:pk>', CategoryDetail.as_view()),
    path('v1', CategoryList.as_view()),
    path('v2/<int:pk>', Sub_CategoryDetail.as_view()),
    path('v2', Sub_CategoryList.as_view()),
    path('v3/<int:pk>', BrandDetail.as_view()),
    path('v3', BrandList.as_view()),
    path('v4/<int:pk>', ProductDetail.as_view()),
    path('v4', ProductList.as_view()),
    path('v5/<int:pk>', Contact_usDetail.as_view()),
    path('v5', Contact_usList.as_view()),
    path('v6/<int:pk>', OrderDetail.as_view()),
    path('v6', OrderList.as_view()),
]