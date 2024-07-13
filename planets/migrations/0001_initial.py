# Generated by Django 5.0.7 on 2024-07-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='planet name')),
                ('planet_id', models.CharField(blank=True, max_length=4)),
                ('wiki_link', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]