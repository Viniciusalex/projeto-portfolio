from email.policy import default
from msilib.schema import Class
from operator import mod
from django.db import models
from datetime import datetime


class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=100)
    linguagem_usada = models.TextField()
    descricao = models.TextField()
    tempo = models.IntegerField()
    categoria = models.CharField(max_length=30)
    data_publicado = models.DateTimeField(default=datetime.now, blank=True)
    foto_projeto = models.ImageField(upload_to='foto/%d/%m/%Y', blank=True)
    projeto_publicado = models.BooleanField(default=False)
    
