
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('<int:projeto_id>', views.projeto, name='projeto'),
    path('buscar', views.buscar, name='buscar'),
    path('criar/projeto', views.criar_projeto, name='criar_projeto' ),
]