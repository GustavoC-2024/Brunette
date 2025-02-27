from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Caja
from django.db.models import Sum
from Ventas.models import Ventas
from Compras.models import Compras
from Empleados.models import Empleados
from django.shortcuts import get_object_or_404

def abrir_caja(request):
    if request.method == 'POST':
        # Obtener el ID del empleado desde el formulario
        id_empleado = request.POST.get('id_empleado')
        monto_inicial = float(request.POST.get('monto_inicial'))

        try:
            empleado = Empleados.objects.get(id_empl=id_empleado)
        except Empleados.DoesNotExist:
            messages.error(request, 'El empleado no existe.')
            return redirect('abrir_caja')

        # Verificar si ya existe una caja abierta para este empleado
        if Caja.objects.filter(id_empl=empleado, abierta_caja=1).exists():
            messages.error(request, 'Este empleado ya tiene una caja abierta.')
            return redirect('abrir_caja')

        try:
            monto_inicial = float(monto_inicial)
            if monto_inicial < 0:
                messages.error(request, 'El monto inicial no puede ser negativo.')
                return redirect('abrir_caja')
        except ValueError:
            messages.error(request, 'El monto inicial debe ser un número válido.')
            return redirect('abrir_caja')

        # Crear nueva caja
        nueva_caja = Caja(
            id_empl=empleado,
            abierta_caja=1,
            monto_inicial_caja=monto_inicial,
            saldo_caja=monto_inicial,
            fecha_hs_aper_caja=timezone.now()
        )
        nueva_caja.save()
        return redirect('menu_caja')  # Redirigir al menú de caja

    # Si no es POST, mostrar el formulario
    empleados = Empleados.objects.all()
    return render(request, 'abrir_caja.html', {'empleados': empleados})

def cerrar_caja(request):
    if request.method == 'POST':
        # Obtener el ID del empleado desde el formulario
        id_empleado = request.POST.get('id_empleado')
        
        try:
            empleado = Empleados.objects.get(id_empl=id_empleado)
            caja = Caja.objects.get(id_empl=empleado, abierta_caja=1)
        except Caja.DoesNotExist:
            messages.error(request, 'El empleado no tiene cajas abiertas.')
            return redirect('cerrar_caja')

        # Calcular ingresos de Ventas (solo las realizadas)
        ingresos = Ventas.objects.filter(
            id_caja=caja,
            venta_realizada=1  # Solo ventas confirmadas
        ).aggregate(total_ingresos=Sum('total_venta'))['total_ingresos'] or 0
        
        # Calcular egresos de Compras
        egresos = Compras.objects.filter(
            id_caja=caja
        ).aggregate(total_egresos=Sum('monto_comp'))['total_egresos'] or 0
        
        # Actualizar caja
        caja.total_ingresos_caja = ingresos
        caja.total_egresos_caja = egresos
        caja.saldo_caja = caja.monto_inicial_caja + ingresos - egresos
        caja.abierta_caja = 0
        caja.fecha_hs_cier_caja = timezone.now()
        caja.save()

        return redirect('resumen_caja', caja_id=caja.id_caja)
    
    # Si no es POST, mostrar el formulario
    empleados = Empleados.objects.all()
    return render(request, 'cerrar_caja.html', {'empleados': empleados})

def resumen_caja(request, caja_id):
    caja = get_object_or_404(Caja, pk=caja_id)
    ventas = Ventas.objects.filter(id_caja=caja)
    compras = Compras.objects.filter(id_caja=caja)
    
    return render(request, 'resumen_caja.html', {
        'caja': caja,
        'ventas': ventas,
        'compras': compras
    })

def menu_caja(request):
    return render(request, 'menu_caja.html')