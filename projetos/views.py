from django.shortcuts import render, get_object_or_404, redirect
from .models import Projeto
from django.contrib.auth.models import User

def index(request):
    # conteudo filtrado por data de publicacao e se vou escolhido para ficar publicado
    projetos = Projeto.objects.order_by('-data_publicado').filter(projeto_publicado=True)

    dados ={
        'projetos' : projetos
    }

    return render(request, 'index.html', dados )

def projeto (request, projeto_id):
    # conteudo mostrado de acordo com a pk
    projeto = get_object_or_404(Projeto, pk=projeto_id)

    projeto_a_exibir= {
        'projeto' : projeto
    }
    return render(request, 'projeto.html', projeto_a_exibir)

def buscar(request):
    lista_projeto = Projeto.objects.order_by('-data_publicado').filter(projeto_publicado= True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_projeto = lista_projeto.filter(nome_projeto__icontains=nome_a_buscar)
    dados = {
        'projetos' : lista_projeto
    }

    return render(request, 'buscar.html', dados)


def criar_projeto(request):
    if request.method == 'POST':
        nome_projeto=request.POST['nome_projeto']
        linguagem_usada=request.POST['linguagem_usada']
        descricao=request.POST['descricao']
        tempo=request.POST['tempo']
        categoria=request.POST['categoria']
        foto_projeto=request.FILES['foto_projeto']
        projeto_publicado=request.POST['projeto_publicado']
        projeto = Projeto.objects.create(nome_projeto=nome_projeto, linguagem_usada=linguagem_usada,descricao=descricao, tempo=tempo, categoria=categoria,foto_projeto=foto_projeto, projeto_publicado=True)
        projeto.save
        return redirect('index')
    else:
        return render(request, 'criar_projeto.html')
