"""medifindDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from medifindapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'accounts/', views.AccountAPIView.as_view(), name='account-list'),
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
    
]
