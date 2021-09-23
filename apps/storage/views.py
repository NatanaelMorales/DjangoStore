from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    allproduct = producto.objects.all()
    return render(request, 'index.html', {'allproduct':allproduct})

def Contact(request):
    return render(request, 'Contact.html')

def About(request):
    return render(request, 'About.html')

def Contacto(request):
    if request.method=='POST':
        correo=request.POST.get('correo')
        nombre = request.POST.get('nombre')
        mensaje=request.POST.get('mensaje')

        print(correo + ' ' + nombre + ' ' + mensaje)

        model_contact = contact(correo=correo,
                                  nombre=nombre,
                                  mensaje=mensaje)
        model_contact.save()
        return redirect('storage:Contacto')

    elif request.method == 'GET':
        return render(request, 'Contact.html')