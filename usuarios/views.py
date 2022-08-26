
from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256 #para nao deixar visivel a senha do usuario na area administrativa.


def login(request):
    if (request.session.get('usuario')):
        return redirect('/livro/home/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status' : status})

def cadastro(request):
    if (request.session.get('usuario')):
        return redirect('/livro/home/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def validar_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, 
                        senha = senha, 
                        email = email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')

    except:
        return redirect('/auth/cadatro/?status=4')

def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest() # cripstografar a senha

    usuario = Usuario.objects.filter(email = email).filter(senha = senha) 
    # trazer do banco de dados algum que tenha email e senha iguais ao solicitados

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')

    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/livro/home/')

        # se a id do usuario esta dentro da session siginifica que o usuário esta autenticado.

    return HttpResponse(f"{email} {senha}")

def sair(request):
    request.session.flush() # apaga completamente a session.
    return redirect('/auth/login/')
   
