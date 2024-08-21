from django.shortcuts import render
from django.http import HttpResponse
from tienda.models import Producto

# Create your views here.
def home(request):
    producto = Producto.objects.all()
    for item in producto:
        print(item.nombre) 
    return render(request, 'tienda/home.html')
