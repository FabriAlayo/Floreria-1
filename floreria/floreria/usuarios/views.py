from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuario ya existe.')
        else:
            User.objects.create_user(username=usuario, email=email, password=password)
            messages.success(request, 'Cuenta creada. Inicia sesión.')
            return redirect('usuarios:login')
    return render(request, 'usuarios/registro.html')