from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sinopse = models.TextField()
    data_lancamento = models.IntegerField(null=True, blank=True)
    episodios = models.IntegerField(null=True, blank=True)
    imagem = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome