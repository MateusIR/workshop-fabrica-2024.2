# Generated by Django 5.0.4 on 2024-08-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0004_alter_anime_imagem_alter_anime_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
