# Generated by Django 5.1.3 on 2024-11-20 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_addtodeck_hider_class_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HiderClass',
            new_name='Hider',
        ),
        migrations.RenameModel(
            old_name='SeekerClass',
            new_name='Seeker',
        ),
    ]
