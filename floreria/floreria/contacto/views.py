from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensaje enviado. Gracias.")
            return redirect('contacto:contacto')
    else:
        form = ContactoForm()
    return render(request, 'contacto/contacto.html', {'form': form})
