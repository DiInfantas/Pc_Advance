from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, "core/index.html")

def contacto (request):
    return render(request, "core/contacto.html")

def catalogo (request):
    return render(request, "core/catalogo.html")

def nosotros (request):
    return render(request, "core/nosotros.html")
