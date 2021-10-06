from random import randint

#1#funções da main 1:
def dadosLab10 (x):
    dado = []
    for i in range(0,x):
        dado.append(randint(1,6))

    return dado


def sequencias_repetidas(lista):
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
        x = int(input('\nquantas vezes vai jogar o dado? \n'))

        jogadas = dadosLab10(x)
        repetidas = sequencias_repetidas(jogadas)

        print('\nresultado:')
        print(str.format('\nEsse e o resultado das {} jogadas feitas = {} ==> mumero de sequencias de faces repetidas {}',x,jogadas,len(repetidas)))
        print('\npara jogar novamente digite (1):')
        print('\npara encerrar o programinha digite (2)')
        
        y = int(input('\ndigite aqui:'))
        
        if y == 1:
            print('\nok, vamos lá! Recomeçando...\n')
            

        if y == 2:
            print('\nencerrando o programinha...')
            print('\nTchau...')
            
    

            
    
    
        
        

#2#funções da main 2:
def areaDoTrapezio(a,b,c):
    return ((a+b)*c)/2

def multiplica_valores(a,b,c):
    return a*a,b*b,c*c

def media_valores(a,b,c):
    return (a+b+c)/3

def variacao(a,b,c):
    return sum(list(range(a,b,c)))

def Variacao_lista(a,b,c):
    return list(range(a,b,c))

#main --- 2#
def main2():

    i = 0

    while i !=5:
        print('digite(1) para area do trapezezio.')
        print('digite(2) para multiplicar os valores.')
        print('digite(3) para verificar a media desses valores.')
        print('digite(4) para somar a variação.')
        print('digite(5) para encerrar')

        i = int(input('digite aqui:\n'))

        if i == 1:
            print('ok, você quer verificar a area de um trapezio.')
            a = int(input('digite a base menor do trapezio:'))
            b = int(input('digite a base maior do trapezio:'))
            c = int(input('digite a altura do trapezio:'))
            
            A = areaDoTrapezio(a,b,c)
            
            print(str.format('essa e a area do trapezio {}',A))
            print('\nmais alguma coisa?\n')

        if i ==2:
            print('aaaah ok, você quer multiplicar um número por ele mesmo, me fale 3...')
            a = int(input('digite um numero inteiro:'))
            b = int(input('digite outro numero inteiro:'))
            c = int(input('so mais um numero inteiro:'))

            B = multiplica_valores(a,b,c)

            print(str.format('Bom, esse foi o resultado {}*{} = {}',a,a,B[0]))
            print(str.format('Bom, esse foi o resultado {}*{} = {}',b,b,B[1]))
            print(str.format('Bom, esse foi o resultado {}*{} = {}',c,c,B[2]))
            print('\nmais alguma coisa?\n')

        if i ==3:
            print('valeu! entao vamos verificar a média entre os valores.')
            a = int(input('primeiro numero:'))
            b = int(input('segundo numero:'))
            c = int(input('terceiro numero:'))

            C = media_valores(a,b,c)

            print(str.format('Essa e a média:{}', C ))
            print('\nmais alguma coisa?\n')

        if i ==4:
            print('então, vamos verificar a soma de uma sequencia com uma variação.')
            a = int(input('digite o primeiro numero da sequência:'))
            b = int(input('digite o limite da sequencia:'))
            c = int(input('digite a variação da sequencia:'))

            D = variacao(a,b,c)
            E = Variacao_lista(a,b,c)
            

            print(str.format('Resultado: lista ={}, soma da lista ==> {}',E,D))
            print('\nmais alguma coisa?\n')


        if i == 5:
            print('\nfinalizando o programinha...')
            print('\nobrigado, até a proxima!')
            print('Bye ...')




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

        if i == 1:
            print('\nvamos continuar...')

        if i ==2:
            print('\nprograminha encerrado\n')
        
    

    
    



    
    
            

                  
        
    

    

            
        
    
        
