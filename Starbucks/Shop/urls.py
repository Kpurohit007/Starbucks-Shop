from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order_view, name='order_view'),
]
