from ast import Pass
from cProfile import label
from datetime import datetime
from tkinter import Widget
from typing import Text
from django import forms
from tempus_dominus.widgets import DatePicker # faz o import da propriedade para que possamos usar e inforrmar o campo que terá o formato de data
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm): #classe que gera os inputs
    data_pesquisa = forms.DateField(label='Data da Pesquisa:', disabled=True, initial=datetime.today)
    class Meta: #serve para manipulaar as infos que estão no modelo para gerar o formulario
        model = Passagem # model recebe o modelo base
        fields = '__all__' # quais campos a serem exibidos
        labels = {'data_ida':'Data de ida', 'data_volta':'Data de volta', 'data_pesquisa':'Data da pesquisa', 'observacoes':'Observações', 'classe_viagem':'Classe do vôo'}
        widgets = {
            'data_ida':DatePicker(),
            'data_volta':DatePicker(),
        }

    def clean(self): # função geral para fazer a validação de campos iguais
        origem = self.cleaned_data.get('origem') # pega o valor dos campos
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        
        lista_erros = {}

        origem_destino_iguais(origem, destino, lista_erros)
        valida_textos(origem, 'origem', lista_erros)
        valida_textos(destino, 'destino', lista_erros)
        valida_data_ida_e_volta(data_ida, data_volta, lista_erros)
        valida_data_hoje(data_ida, data_pesquisa, lista_erros)

        if lista_erros is not None: #verifica se a lista está vazio
            for erro in lista_erros: #se não estiver, atribui para cada lista, um erro
                mensagem_erro = lista_erros[erro] #cria umaa var incluindo na lista de erros um erro
                self.add_error(erro, mensagem_erro) # atribui no campo o erro, sendo onde será que vai ser o erro e a mensagem do erro
        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome'] #traz todos os campos exceto o nome
