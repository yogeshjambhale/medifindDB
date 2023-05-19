from rest_framework import serializers

from .models import User, Account, Products,CartData,UserSignup,AdminSignup,Address,Orders

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"



class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class CartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartData
        fields = "__all__"

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = "__all__"

class AdminSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminSignup
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"