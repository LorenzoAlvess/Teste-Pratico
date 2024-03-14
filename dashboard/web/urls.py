# urls.py

from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.home, name='home'),
    path('bibliotecas/', views.bibliotecas, name='bibliotecas'),
    path('bibliotecas/<int:biblioteca_id>/livros/', views.livros, name='livros'),
    path('graficos/', views.graficos, name='graficos'),
]
