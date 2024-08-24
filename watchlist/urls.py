from django.urls import path
from .views import add_to_watchlist, watchlist_view

urlpatterns = [
    path('adicionar/<int:anime_id>/', add_to_watchlist, name='add_to_watchlist'),
    path('minha-watchlist/', watchlist_view, name='watchlist_view'),
]