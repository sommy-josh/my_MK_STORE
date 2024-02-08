from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'




class CategorySerializer(serializers.ModelSerializer):
    
     class Meta:
        model = Category
        fields =('id', 'name', 'description', 'image', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    CATEGORY_CHOICES=Product.CATEGORY_CHOICES
    category=serializers.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Product
        fields = ('id', 'product_name','size', 'description', 'price', 'quantity', 'category', 'image', 'date_added')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'