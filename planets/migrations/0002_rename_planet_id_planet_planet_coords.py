# Generated by Django 5.0.7 on 2024-07-13 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='planet_id',
            new_name='planet_coords',
        ),
    ]
