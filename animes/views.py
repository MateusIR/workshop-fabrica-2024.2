import requests
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BuscaAnimeForm
from .models import Anime

def buscar_anime(request):
    if request.method == 'POST':
        form = BuscaAnimeForm(request.POST)
        if form.is_valid():
            nome_anime = form.cleaned_data['nome']
            response = requests.get(f'https://api.jikan.moe/v4/anime?q={nome_anime}&sfw')
            if response.status_code == 200:
                dados = response.json()
                if dados['data']:
                    dados_anime = dados['data'][0]
                    anime = Anime(
                        nome=dados_anime.get('title'),
                        sinopse=dados_anime.get('synopsis'),
                        data_lancamento=dados_anime.get('year'),
                        episodios=dados_anime.get('episodes'),
                        imagem=dados_anime.get('images', {}).get('jpg', {}).get('image_url'),
                        )
                    anime.save()
                    return redirect('listar_animes')
                else:
                    form.add_error(None, "erro ao buscar o anime.")
    else:
        form = BuscaAnimeForm()

    return render(request, 'buscar_anime.html', {'form': form})



def listar_animes(request):
    animes = Anime.objects.all()
    return render(request, 'listar_animes.html', {'animes': animes})

def deletar_anime(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        anime.delete()
        return redirect('listar_animes')
    return render(request, 'deletar_anime.html', {'anime': anime})