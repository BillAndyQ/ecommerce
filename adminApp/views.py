from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def home(request):
    html_content = "<h1>Bienvenido a mi app Admin</h1><p>Este es un texto en HTML.</p>"
    return HttpResponse(html_content)