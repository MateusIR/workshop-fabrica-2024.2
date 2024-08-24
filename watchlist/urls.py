from django.urls import path
from . import views
from .views import add_watchlist, watchlist_view

urlpatterns = [
    path('adicionar/<int:anime_id>/', add_watchlist, name='add_to_watchlist'),
    path('minha-watchlist/', watchlist_view, name='watchlist_view'),
    path('remover/<int:anime_id>/', views.remover_da_watchlist, name='remove_from_watchlist'),
]