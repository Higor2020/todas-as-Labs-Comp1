from random import randint

def dados ():
    '''A função simula o numero de jogadas feitas até dois dados sairem com numeros iguais;
        resultado esperado: int
    '''

    y = 0
    dados =[]
    dados.append((randint(1,6),randint(1,6)))

    while dados[y][0]!= dados[y][1]:
        dados.append((randint(1,6),randint(1,6)))
        y+=1

    return len(dados)
             

                
def busca (setor,matriz):
    
    '''A função recebe um nome de um setor(str) e uma agenda com as informações
        dos funcionários como parametros de entrada. A função retorna uma matriz com as informações de todos os
        funcionários daquele setor;
        str,list-->list
    '''
    retornoBusca = []

    for i in range(len(matriz)):
        for setores in matriz[i]:
            if setores == setor:
                list.append(retornoBusca,matriz[i])
    for y in range(len(retornoBusca)):
        if setor in retornoBusca[y]:
            retornoBusca[y].remove(setor)
            
    return retornoBusca
    
    
    
