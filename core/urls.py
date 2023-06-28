from django.urls import path 
from .views import index, nosotros, contacto, catalogo, lista_productos, guarda_producto, elimina_producto, form_mod_producto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',index, name="index"),
    path('nosotros/',nosotros, name="nosotros"),
    path('contacto/',contacto, name="contacto"),
    path('catalogo/',catalogo, name="catalogo"),

    path('lista_productos/',lista_productos,name="lista_productos"),
    
    path('guarda_producto/',guarda_producto,name="guarda_producto"),
    path('elimina_producto/<id>',elimina_producto,name="elimina_producto"),
    path('form_mod_producto/<id>',form_mod_producto ,name="form_mod_producto"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)