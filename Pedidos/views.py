from django.shortcuts import render
from .models import Pedidos
from .models import Productos

def lista_pedidos(request):
    estado = request.GET.get('estado', 'todos')  # Captura el filtro de estado desde la URL
    if estado == 'todos':
        pedidos = Pedidos.objects.all()
    else:
        pedidos = Pedidos.objects.filter(
            **{estado + '_ped': 1}  # Filtra según el estado seleccionado
        )

    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos, 'estado': estado})

def lista(request):
    Productos= Productos.objects.all()
    return render(request, "Pedidos/lista_pedidos.html", {"Productos":Productos})

