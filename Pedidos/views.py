from django.shortcuts import render
from .models import Pedidos
from .models import Productos

def lista_pedidos(request):
    estado = request.GET.get('estado', 'todos')
    pedidos = Pedidos.objects.all() if estado == 'todos' else Pedidos.objects.filter(**{f'{estado}_ped': 1})
    productos = Productos.objects.all()  # <-- Añade esta línea
    return render(request, 'pedidos/lista_pedidos.html', {
        'pedidos': pedidos,
        'estado': estado,
        'productos': productos  # <-- Pasa los productos al template
    })

def lista(request):
    Productos= Productos.objects.all()
    return render(request, "Pedidos/lista_pedidos.html", {"Productos":Productos})


