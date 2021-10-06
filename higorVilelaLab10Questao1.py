from random import randint

#1#funções da main 1:
def dados(x):
    '''A função recebe a quantidade de lances que um dado será jogado
        e gera uma lista com as faces que sairam nos lances;
        int --> list
    '''
    dado = []
    for i in range(0,x):
        dado.append(randint(1,6))

    return dado


def sequencias_repetidas(lista):
    '''A função recebe uma lista de numeros inteiros e detecta as sequencias
        da lista que repetiram gerando uma nova lista; list --> list
    '''
    lst = []
    for i  in range(len(lista)):
        if lista[i-1]== lista[i]:
                lst.append(lista[i])
    return lst
                    
#main - 1#
def main1():
    y=0
    while y !=2:
        print('----------lançamentos de aum dado---------------')
        
        #entrada do numero de vezes que o jogador vai jogar o dado#
        x = int(input('\nquantas vezes vai jogar o dado? \n'))

        #chamada das funções alocadas em variaveis#
        jogadas = dadosLab10(x)
        repetidas = sequencias_repetidas(jogadas)

        #resultado imprimido com a contagem das sequencias#
        print('\nresultado:')
        print(str.format('\nEsse e o resultado das {} jogadas feitas = {} ==> mumero de sequencias de faces repetidas {}',x,jogadas,len(repetidas)))

        #Entrada de dados para sugerir ao jogador oque fazer logo apos o resultado#
        print('\npara jogar novamente digite (1):')
        print('\npara encerrar o programinha digite (2)')
        
        y = int(input('\ndigite aqui:'))

        #condicionais da variavel y do programa de acordo com o input feito#
        if y == 1:
            print('\nok, vamos lá! Recomeçando...\n')
            

        if y == 2:
            print('\nencerrando o programinha...')
            print('\nTchau...')
            
