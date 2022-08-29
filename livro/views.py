from datetime import date, datetime
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Emprestimos, Livros, Categoria
from django import forms
from .forms import CadastroLivro

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

        return render(request, 'home.html', {'livros': livros, 'usuario_logado': request.session.get('usuario'), 'form': form})
    
    else:
        return redirect('/auth/login/?status=2')
    

def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livros)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            

            return render(request, 'ver_livro.html', {'livro': livros,     
                                                      'categoria_livro': categoria_livro, 'emprestimos': emprestimos,
                                                      'usuario_logado':request.session.get('usuario'), 'form': form})
            
            # nao vai permitir que o usuário acesse direto pela barra de navegação.
        else:
            return HttpResponse('este livro nao é seu')
    return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST) #instancia
        
        if form.is_valid():
            form.save()
            return redirect('/livro/home')
        else:
            return HttpResponse('Dados inválidos')
            


    