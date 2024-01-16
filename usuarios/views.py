from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def cadastrar (request):

    if request.method == "GET":
        return render (request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são idênticas')
            return redirect('/usuarios/cadastro')

        user = User.objects.filter(username__iexact=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'O usuário já é existente')
            return redirect('/usuarios/cadastro')
        
        try:
            user = User.objects.create_user(username=username, password=senha)
            messages.add_message(request,constants.SUCCESS, f'{user.username} foi cadastro com sucesso')
            return redirect('/usuarios/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do seriviço')
            return redirect('/usuarios/cadastro')
        
def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse("Já estou logado")
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            messages.add_message(request, constants.SUCCESS, f'{user.username} logado com sucesso')
            return HttpResponse("teste")
        else:
            messages.add_message(request, constants.ERROR, "Usuário ou senha inválidos")
            return redirect('/usuarios/logar')

def sair(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, 'Você não esta mais logado')
    return redirect('/usuarios/logar')