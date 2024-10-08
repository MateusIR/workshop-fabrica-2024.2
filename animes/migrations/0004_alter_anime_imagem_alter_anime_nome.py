# Generated by Django 5.0.4 on 2024-08-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_alter_anime_data_lancamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='imagem',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
