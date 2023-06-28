from django import forms
from django.forms import ModelForm
from .models import Producto

class ProductoFormulario(ModelForm):
    class Meta:
        model = Producto
        fields=['idProducto', 'nombre', 'precio','modelo','categoria']