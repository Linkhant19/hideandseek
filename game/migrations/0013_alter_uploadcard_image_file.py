# Generated by Django 5.1.3 on 2024-12-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_rename_image_uploadcard_image_file_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcard',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]