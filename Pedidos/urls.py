from django.urls import path
from . import views

urlpatterns = [
    path('Pedidos', views.lista_pedidos, name='lista_pedidos'),
    path('nuevo/', views.crear_pedido, name='nuevo_pedido'),
    path('Pedidos', views.pedidos_guardados, name='pedidos_guardados'),
    
]
