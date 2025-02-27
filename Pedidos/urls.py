from django.urls import path
from . import views

urlpatterns = [
    path('Pedidos', views.lista_pedidos, name='lista_pedidos'),
]
