#3#
def busca(j,x):
    
    '''A função recebe um nome de um setor(str) e uma agenda com as informações
        dos funcionários como parametros de entrada. A função retorna uma matriz com as informações de todos os
        funcionários daquele setor;
        str,list-->list
    '''
    retornoBusca = []

    for i in range(len(x)):
        for setores in x[i]:
            if setores == j:
                list.append(retornoBusca,x[i])
    for y in range(len(retornoBusca)):
        if j in retornoBusca[y]:
            retornoBusca[y].remove(j)
            
    return retornoBusca


def main3():
    
    i = 0
    while i !=2:
        print( '>>> Busca de funcionários <<<\n')
        print( 'ATENÇÂO: para fazer a busca, insira a matriz com as informações')
        print( 'e depois o setor que será buscado.\n')
    
        x = input('Insira a matriz:\n')
    
        j = str(input('Insira o setor aqui:\n'))

        w = busca(j,x)

        print(str.format('Segue o resultado da pesquisa --> {}',w))

        if w == []:
            print('\nNenhum registro encontrado...\n')

        print('\nPara continuar digite (1)\n')
        print('\nPara encerrar o programinha digite (2)\n')
        int(input('digite aqui:'))

        if i == 1:
            print('\nvamos continuar...')

        if i == 2:
            print('\nprograminha encerrado\n')

        
        
