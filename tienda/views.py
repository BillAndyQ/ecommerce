from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html_content = "<h1>Bienvenido a mi aplicación Django</h1><p>Este es un texto en HTML.</p>"
    return HttpResponse(html_content)