from django.shortcuts import render
from rest_framework import generics

from .models import User, Account, Products,CartData,UserSignup,AdminSignup,Address,Orders
from .serializers import AccountSerializer,  ProductsSerializer,CartDataSerializer,UserSignupSerializer,AdminSignupSerializer,AddressSerializer,OrdersSerializer

class AccountAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class ProductsAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    lookup_field = 'pk'
    serializer_class = ProductsSerializer
    
class productAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CartDataAPIView(generics.ListCreateAPIView):
    queryset = CartData.objects.all()
    serializer_class = CartDataSerializer

class CartDataIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartData.objects.all()
    lookup_field = 'userId'
    serializer_class = CartDataSerializer

class UserSignupAPIView(generics.ListCreateAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer

class UserSignupIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserSignup.objects.all()
    serializer_class = UserSignupSerializer

class AdminSignupAPIView(generics.ListCreateAPIView):
    queryset = AdminSignup.objects.all()
    serializer_class = AdminSignupSerializer

class AddressAPIView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class OrdersAPIView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class OrdersIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    lookup_field = 'userId'
    serializer_class = OrdersSerializer
