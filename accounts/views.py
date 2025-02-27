from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Datos incorrectos. Intente nuevamente.")
        return super().form_invalid(form)
    
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Sesión cerrada con éxito.")
        return super().dispatch(request, *args, **kwargs)