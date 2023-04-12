from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais')
            return redirect(reverse('cadastro'))

        if len(senha) < 4:
            messages.add_message(request, constants.ERROR, 'A senha deve ser maior ou igual a 4 digitos.')
            return redirect(reverse('cadastro'))
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe!')
            return redirect(reverse('cadastro'))   
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso!')
        return redirect(reverse('login'))
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')