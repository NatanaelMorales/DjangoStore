from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allproduct = producto.objects.all()
    return render(request, 'index.html', {'allproduct':allproduct})

def Contact(request):
    return render(request, 'Contact.html')

def About(request):
    return render(request, 'About.html')

def Home(request):
    return render(request, 'Home.html')