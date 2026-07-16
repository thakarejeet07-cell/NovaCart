from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
]
