
from django.contrib import admin
from django.urls import path , include
from medifindapp import views
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/user/', include('medifindapp.urls')) ,   
    path('products/',views.ProductsAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/',views.productAPIView.as_view(), name='product-list'),
    path(r'cartdata/',views.CartDataAPIView.as_view(), name='product-list'),
    path(r'cartdataid/<int:userId>/',views.CartDataIdAPIView.as_view(), name='product-list'),
    path(r'user-signup/',views.UserSignupAPIView.as_view(), name='product-list'),
    path(r'user-signup-id/<int:pk>/',views.UserSignupIdAPIView.as_view(), name='product-list'),
    path(r'admin-signup/',views.AdminSignupAPIView.as_view(), name='product-list'),
    path(r'address/',views.AddressAPIView.as_view(), name='product-list'),
    path(r'orders/',views.OrdersAPIView.as_view(), name='product-list'),
    path(r'order/<int:userId>/',views.OrdersIdAPIView.as_view(), name='product-list'),

    path(r'hotels/',views.HotelAPIView.as_view(), name='product-list'),
    path(r'hotel/<int:id>/',views.HotelIdAPIView.as_view(), name='product-list'),
    path(r'rooms/',views.RoomsAPIView.as_view(), name='product-list'),
    path(r'room/<int:id>/',views.RoomsIdAPIView.as_view(), name='product-list'),
    
]
