# Generated by Django 4.1.2 on 2022-10-13 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_projeto', models.CharField(max_length=100)),
                ('linguagem_usada', models.TextField()),
                ('descricao', models.TextField()),
                ('tempo', models.IntegerField()),
                ('categoria', models.CharField(max_length=30)),
                ('data_publicado', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
