# Generated by Django 5.0.4 on 2024-08-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0002_anime_episodios_anime_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='data_lancamento',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
