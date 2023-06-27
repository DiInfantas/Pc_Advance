from django.urls import path 
from .views import index, nosotros, contacto, catalogo

urlpatterns=[
    path('',index, name="index"),
    path('nosotros/',nosotros, name="nosotros"),
    path('contacto/',contacto, name="contacto"),
    path('catalogo/',catalogo, name="catalogo"),

]