#1#a#

def deletaNum(lista,excluir_numero):

    ''' A função recebe dois parametros a lista de infomações
        e o numero que deve ser deletado da listagem, caso o telefone não esteja listado
        nada será feito e retornará False e True para se caso o numero exista e foi deletado.
        list,str-->bool      
    ''' 
    if  excluir_numero in lista[1]:
        lista[1].remove(excluir_numero)
        return True 

    else:
        return False



    
    
#2#
def campeonato_carioca(tabela):

    ''' A função recebe uma tabela de campeonato no formato dicionário e retorna uma lista com:
        uma sublista da tabela, a média de pontos por time e o total de pontos do time campeão;
        dicionario --> lista
    '''

    pontos = list(dict.values(tabela))

    time = list(dict.keys(tabela))

    tabela_campeonato = list(dict.items(tabela))
        
    media_pontos = sum(pontos)/len(time)

    campeao = max(pontos)

    
    return [tabela_campeonato , media_pontos , campeao]

    
