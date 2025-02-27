from django.urls import path
from Cajas import views

urlpatterns = [
    path('menu-caja/', views.menu_caja, name='menu_caja'),
    path('abrir-caja/', views.abrir_caja, name='abrir_caja'),
    path('cerrar-caja/', views.cerrar_caja, name='cerrar_caja'),
    path('resumen-caja/<int:caja_id>/', views.resumen_caja, name='resumen_caja'),
]