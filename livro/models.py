
from django.db import models
from datetime import date
import datetime
from django.db.models.base import Model
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome



class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True, null = True) 
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default=False, null = True)
    nome_emprestado = models.CharField(max_length = 30, blank = True, null = True)
    data_emprestimo = models.DateTimeField(blank = True, null = True)
    data_devolução = models.DateTimeField(blank = True, null = True)
    tempo_duração = models.DateTimeField(blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    

    # blanck = True para toranar o item não obrigatório no cadastro. (vazio)
    # null = True permite o valor null. (Nulo)
    
    class Meta:
        verbose_name = 'Livro'

    def __str__(self) -> str: 
        return self.nome


    
