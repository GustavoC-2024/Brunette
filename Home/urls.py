from django.urls import path
from Home import views

urlpatterns = [ 
    path('',views.PagPrincipal, name='Pag-Principal'),
    path('logout/', views.logout_view, name='logout'),
]