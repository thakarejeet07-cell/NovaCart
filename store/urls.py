from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name="add_to_cart"),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name="remove_from_cart"), 
]
