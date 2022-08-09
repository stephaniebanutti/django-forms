from ast import Pass
from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms
from passagens.models.pessoa import Pessoa


def index(request):
    form = PassagemForms() # Recebe minha class
    pessoa_form = PessoaForms
    contexto = {'form': form, 'pessoa_form': pessoa_form} # Fez um dict com o valor da class
    return render(request, 'index.html', contexto) # Recebe contexto em formato de dict para poder transferir pro HTML


def revisao_consulta(request):
    if request.method == 'POST': #Verifica se o metodo que vem pra cá é tipo POST
        form = PassagemForms(request.POST) #Recebe os valores que vem da class
        pessoa_forms = PessoaForms(request.POST) #Recebe os valores que vem da class
        if form.is_valid():
            contexto = {'form': form, 'pessoa_forms': pessoa_forms} # Fez um dict com o valor da class
            return render(request, 'minha_consulta.html', contexto) # Recebe contexto em formato de dict para poder transferir pro HTML
        else:
            print("Form inválido.")
            contexto = {'form': form} # Fez um dict com o valor da class
            return render(request, 'index.html', contexto) # Recebe contexto em formato de dict para poder transferir pro HTML
        
