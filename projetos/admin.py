from django.contrib import admin
from .models import Projeto

class ListandoProjetos(admin.ModelAdmin):
    # o que vai aparecer na tela do admin
    list_display = ('id', 'nome_projeto', 'linguagem_usada', 'projeto_publicado')
    # locais que vão ser clicaveis
    list_display_links =('id', 'nome_projeto')
    # criar um filtro 
    list_filter = ('nome_projeto', 'linguagem_usada', 'categoria',)
    # criar barra de pesquisa
    search_fields = ('nome_projeto',)
    # limitar conteudos por pagina
    list_per_page = 3
    # conteudo poder ser editado sem entrar no conteudo 
    list_editable = ('projeto_publicado',)
admin.site.register(Projeto,ListandoProjetos)


