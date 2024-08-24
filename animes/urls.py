
from django.urls import path, include
from animes.views import buscar_anime, listar_animes, deletar_anime

urlpatterns = [
    path('', buscar_anime, name='buscar_anime'),
    path('animes/', listar_animes, name='listar_animes'),
    path('animes/deletar/<int:pk>/', deletar_anime, name='deletar_anime'),
]