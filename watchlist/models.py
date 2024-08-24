from django.db import models
from animes.models import Anime


# Create your models here.

class Watchlist(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.anime.nome)
