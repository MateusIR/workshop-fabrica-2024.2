# Generated by Django 5.0.4 on 2024-08-24 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0002_watchlist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='user',
        ),
    ]
