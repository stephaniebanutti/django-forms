def origem_destino_iguais(origem, destino, lista_erros):
    """ Verifica se destino e origem são iguais """
    if origem == destino:
        lista_erros['destino'] = ('Origem e destino não podem ser iguais.')# na lista_erros[campo que aparece a msg] = mensagem a ser atribuida
    
def valida_textos(valor_campo, nome, lista_erros):
    """ Faz a verificação se existem números no campo texto """
    if any(char.isdigit() for char in valor_campo): # primeira parte verifica se tem numero, se tiver, para cada número dentro do meu campo origem, retorna mensagem de erro
        lista_erros[nome] = ('Campo inválido, não inclua números.')


def valida_data_ida_e_volta(data_ida, data_volta, lista_erros):
    """ Verifica se a data de ida é maior que a data de volta """
    if data_ida > data_volta:
        lista_erros['data_volta'] = ('A data de volta não pode ser menor que a data de volta.')


def valida_data_hoje(data_ida, data_pesquisa, lista_erros):
    """ Verifica se a data de ida é maior que a data de hoje """
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = ('A data de ida não pode ser menor que hoje.')
