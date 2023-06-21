from django.urls import path , include
from medifindapp import views

urlpatterns = [
    path ('register/', views.UserRegistrationView.as_view(), name='register'),
]