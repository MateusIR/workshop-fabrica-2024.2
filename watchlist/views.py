
from django.shortcuts import render, redirect, get_object_or_404
from .models import Watchlist
from .models import Anime
from .forms import AddToWatchlistForm

# Create your views here.


def add_watchlist(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    Watchlist.objects.create(anime=anime)
    return redirect('listar_animes')



def watchlist_view(request):
    watchlist_items = Watchlist.objects.all()
    return render(request, 'watchlist.html', {'watchlist': watchlist_items})

def remover_da_watchlist(request, anime_id):
    watchlist_item = get_object_or_404(Watchlist, anime__id=anime_id)
    watchlist_item.delete()
    return redirect('watchlist_view')
