from django.urls import path 
from .views import index, nosotros, contacto, catalogo, lista_productos, guarda_producto, elimina_producto, form_mod_producto

urlpatterns=[
    path('',index, name="index"),
    path('nosotros/',nosotros, name="nosotros"),
    path('contacto/',contacto, name="contacto"),
    path('catalogo/',catalogo, name="catalogo"),

    path('catalogo/',lista_productos,name="lista_productos"),
    
    path('guarda_producto/',guarda_producto,name="guarda_producto"),
    path('elimina_producto/<id>',elimina_producto,name="elimina_producto"),
    path('form_mod_producto/<id>',form_mod_producto ,name="form_mod_producto"),

]