from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import User,  Products,CartData,UserSignup,AdminSignup,Address,Orders,rooms,hotel
from .serializers import   ProductsSerializer,CartDataSerializer,UserSignupSerializer,AdminSignupSerializer,AddressSerializer,OrdersSerializer,UserRegistrationSerializer,RoomSerializer,HotelSerializer




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

class UserRegistrationView(APIView):
    def post(self, request,):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Successfull'},
            status.status.HTTP_201_CREATED)

        return Response(serializer.errors, status.status.HTTP_400_BAD_REQUEST)

class HotelAPIView(generics.ListCreateAPIView):
    queryset = hotel.objects.all()
    serializer_class = HotelSerializer

class HotelIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = hotel.objects.all()
    lookup_field = 'id'
    serializer_class = HotelSerializer

class RoomsAPIView(generics.ListCreateAPIView):
    queryset = rooms.objects.all()
    serializer_class = RoomSerializer

class RoomsIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = rooms.objects.all()
    lookup_field = 'id'
    serializer_class = RoomSerializer