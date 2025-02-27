from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def PagPrincipal(request):
    datos = {
        'nombre': 'Brunette'
    }

    return render(request, 'home1.html', datos)

def logout_view(request):
    pass