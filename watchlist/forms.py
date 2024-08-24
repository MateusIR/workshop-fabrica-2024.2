from django import forms

from watchlist.models import Watchlist


class AddToWatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = []