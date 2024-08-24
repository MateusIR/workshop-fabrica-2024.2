from django import forms

from .models import Watchlist

class AddToWatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['anime']