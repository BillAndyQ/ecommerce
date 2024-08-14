from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Cambia 'home' por la vista que desees
    # Otras rutas de la app
]
