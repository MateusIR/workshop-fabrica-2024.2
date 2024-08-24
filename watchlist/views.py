from django.shortcuts import render, redirect, get_object_or_404

import watchlist
from .models import Watchlist
from .models import Anime
from .forms import AddToWatchlistForm

# Create your views here.


def add_to_watchlist(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)

    # Verifica se o anime já está na watchlist do usuário

    if not Watchlist.objects.filter(anime=anime).exists():
        Watchlist.objects.create(anime=anime)
    return redirect('listar_animes')  # Redireciona para a lista de animes


def watchlist_view(request):
    return render(request, 'watchlist.html', {'watchlist': watchlist})


