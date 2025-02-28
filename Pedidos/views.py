from django.shortcuts import render
from .models import Pedidos
from .models import Productos, Mesas

def lista_pedidos(request):
    estado = request.GET.get('estado', 'todos')
    pedidos = Pedidos.objects.all() if estado == 'todos' else Pedidos.objects.filter(**{f'{estado}_ped': 1})
    productos = Productos.objects.all()
    mesas = Mesas.objects.all()  # <-- Obtén todas las mesas
    return render(request, 'pedidos/lista_pedidos.html', {
        'pedidos': pedidos,
        'estado': estado,
        'productos': productos,
        'mesas': mesas  # <-- Pasa las mesas al template
    })

def pedidos_guardados(request):
    pedidos= Pedidos.objects.all()
    return render(request, "Pedidos/pedidos_guardados.html", {"Pedidos":Pedidos})


