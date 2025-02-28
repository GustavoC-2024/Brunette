from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from .models import Pedidos, DetallePed
from Mesas.models import Mesas
from Productos.models import Productos
from Cajas.models import Caja

def lista_pedidos(request):
    estado = request.GET.get('estado', 'todos')
    pedidos = Pedidos.objects.all() if estado == 'todos' else Pedidos.objects.filter(**{f'{estado}_ped': 1})
    productos = Productos.objects.all()
    mesas = Mesas.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {
        'pedidos': pedidos,
        'estado': estado,
        'productos': productos,
        'mesas': mesas
    })

@csrf_exempt
@require_http_methods(["POST"])
def crear_pedido(request):
    try:
        data = json.loads(request.body)
        
        # Validación básica
        if not data.get('mesa_id'):
            return JsonResponse({'success': False, 'error': 'Seleccione una mesa'}, status=400)
        
        if not data.get('productos') or len(data['productos']) == 0:
            return JsonResponse({'success': False, 'error': 'Agregue al menos un producto'}, status=400)

        # Obtener mesa
        mesa = Mesas.objects.get(id_mesa=data['mesa_id'])
        
        # Crear pedido principal
        nuevo_pedido = Pedidos.objects.create(
            id_mesa=mesa,
            generado_ped=1,
            proceso_ped=0,
            listo_ped=0,
            entregado_ped=0,
            pagado_ped=0,
            fecha_gen_ped=timezone.now().date(),
            hora_gen_ped=timezone.now().time()
        )
        
        # Procesar productos
        total_pedido = 0
        for producto in data['productos']:
            try:
                prod = Productos.objects.get(id_prod=producto['id_producto'])
            except Productos.DoesNotExist:
                nuevo_pedido.delete()
                return JsonResponse({'success': False, 'error': f'Producto ID {producto["id_producto"]} no existe'}, status=400)
            
            # Crear detalle
            detalle = DetallePed.objects.create(
                id_pedido=nuevo_pedido,
                id_prod=prod,
                precio_uni_ped=producto['precio'],
                cantidad_ped=producto['cantidad'],
                sub_total_ped=float(producto['precio']) * int(producto['cantidad']),
                total_ped=float(producto['precio']) * int(producto['cantidad'])
            )
            
            total_pedido += detalle.total_ped
        
        # Actualizar total del pedido
        nuevo_pedido.total_ped = total_pedido
        nuevo_pedido.save()
        
        return JsonResponse({
            'success': True,
            'message': f'Pedido #{nuevo_pedido.id_pedido} guardado exitosamente',
            'pedido_id': nuevo_pedido.id_pedido
        })
        
    except Mesas.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Mesa no encontrada'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

def pedidos_guardados(request):
    pedidos = Pedidos.objects.all().order_by('-fecha_gen_ped')
    return render(request, "pedidos/pedidos_guardados.html", {"pedidos": pedidos})


