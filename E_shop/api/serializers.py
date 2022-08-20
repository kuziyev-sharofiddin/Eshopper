from rest_framework import serializers
from app.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Sub_Category
        fields='__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class Contact_usSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact_us
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'