#1#

#a#
def contatinhosapp_novocontato(nome,telefone ='',email='',instagram=''):
    ''' A funçao recebe 4 parametros : nome, telefone,email e instagram. 
        Com essas infomações é gerada uma lista do novo contato;
        str,list,str,str -> list
    '''

    contatinhosapp = []
    contatinhosapp.append(nome)
    contatinhosapp.append(telefone)
    contatinhosapp.append(email)
    contatinhosapp.append(instagram)

    
    return contatinhosapp


#b#
def atualiza_app_informacoes (lista,parametro_antigo,parametro_novo):

    ''' A função recebe como parametro a lista que deve ser alterada,
        o parametro antingo que deseja alterar e o parametro novo que deve ficar no lugar.
        True para atualização feita e false para valor ja existe;
        list,str,str --> bool
    '''

    y = lista.index(parametro_antigo)
    lista.insert(y,parametro_novo)
    lista.remove(parametro_antigo)

    if parametro_novo != parametro_antigo:
        return True 

    else:
        return False
    


def atualiza_app_telefone(lista,telefone_novo,telefone_antigo):

    ''' A função recebe a lista que deve ser alterada,
        o telefeno a ser incluido e o telefone que deve ser descartado.
        Será retornado True para atualização feita e False para valor ja existe;
        list,str,str --> bool
    '''

    y=lista[1].index(telefone_antigo)
    lista[1].insert(y,telefone_novo)
    lista[1].remove(telefone_antigo)

    
    if telefone_novo != telefone_antigo:
          return True 

    else:
        return False



#2#

def aminoacido (RNA):

    '''A função recebe uma molecula mensageira de RNA(STRING MAIUSCULA) e a traduz para uma cadeia de aminoacidos;
        str --> str
    '''

    trincaRna = { 'UUU': 'Phe', 'CUU':'Leu', 'UUA': 'Leu', 'AAG':'Lisina', 'UCU':'Ser','UAU':'Tyr','CAA':'Gln'}

    
    return trincaRna[RNA[0:3]]+'-'+trincaRna[RNA[3:6]]+'-'+trincaRna[RNA[6:9]]

    


