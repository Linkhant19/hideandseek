# Generated by Django 5.1.3 on 2024-12-04 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_profile_favorite_card_delete_favoritecard'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.profile')),
            ],
        ),
    ]