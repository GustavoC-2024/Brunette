from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Productos

@require_GET
def buscar_productos(request):
    term = request.GET.get('term', '')
    productos = Productos.objects.filter(nombre_prod__icontains=term)[:10]  # Limita a 10 resultados
    resultados = [
        {
            'id': producto.id_prod,
            'nombre': producto.nombre_prod,
            'precio': producto.precio_prod
        } 
        for producto in productos
    ]
    return JsonResponse(resultados, safe=False)
