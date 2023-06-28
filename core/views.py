from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoFormulario

# Create your views here.

def index (request):
    return render(request, "core/index.html")

def contacto (request):
    return render(request, "core/contacto.html")

def catalogo (request):
    return render(request, "core/catalogo.html")

def nosotros (request):
    return render(request, "core/nosotros.html")

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def guarda_producto(request):
    form = ProductoFormulario
    mensaje = ""

    if request.method == 'POST':
        guarda_producto=ProductoFormulario(request.POST)
        if guarda_producto.is_valid():
            nombre = request.POST.get('nombre', None)
            if nombre in Producto.objects.values_list('nombre', flat=True):
                mensaje = "Este nombre ya existe en la Base de Datos, intente con otro"
            else:
                guarda_producto.save()
                mensaje = "Datos registrados Correctamente"
    return render(request, "core/guarda_producto.html",{"form":form, "mensaje": mensaje })

def form_mod_producto(request, id):
    Producto = Producto.objects.get(idProducto=id) 
    mensaje =""
    if request.method =='POST':
        guarda_producto=ProductoFormulario(request.POST, instance=Producto)
        if guarda_producto.is_valid():                   
            guarda_producto.save()
            mensaje = "Datos actualizados Correctamente"
    return render(request, "core/modifica_producto.html",{"form":ProductoFormulario(instance=Producto),"mensaje":mensaje})

def elimina_producto(request, id):
    Producto = Producto.objects.get(idProducto=id)
    Producto.delete()
    return redirect(to="lista_productos")