from django import forms

from animes.models import Anime


class BuscaAnimeForm(forms.Form):
    nome = forms.CharField(label='Nome do Anime', max_length=100)

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['nome', 'sinopse', 'data_lancamento', 'episodios', 'imagem']