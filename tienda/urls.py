from django.urls import path
from .views import home

urlpatterns = [
    path('', home.home, name='home'),  # Cambia 'home' por la vista que desees
    # Otras rutas de la app
]
