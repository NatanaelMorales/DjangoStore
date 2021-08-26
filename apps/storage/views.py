from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Contact(request):
    return render(request, 'Contact.html')

def About(request):
    return render(request, 'About.html')

def Home(request):
    return render(request, 'Home.html')