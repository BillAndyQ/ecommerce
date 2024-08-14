from django.shortcuts import render
from django.http import HttpResponse
from tienda.models import Producto

# Create your views here.
def home(request):
    producto = Producto.objects.all()
    for item in producto:
        print(item.nombre) 
    html_content = "<h1>Bienvenido a mi aplicación Django Ecommerce</h1><p>Este es un texto en HTML.</p>"
    return HttpResponse(html_content)