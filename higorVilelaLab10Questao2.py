#2#funções da main 2:
def areaDoTrapezio(a,b,c):
    '''Função que identifica a area de um trapezio; int, int, int --> float
    '''
    return ((a+b)*c)/2

def multiplica_valores(a,b,c):
    '''Função que multiplica cada elemento por ele mesmo; int, int, int-->tuple
    '''
    return a*a,b*b,c*c

def media_valores(a,b,c):
    '''Função que identifica a média entre os valores; int,int,int --> float
    '''
    return (a+b+c)/3

def variacao(a,b,c):
    '''Função que soma a sequencia com a variação; int,int,int --> float
    '''
    return sum(list(range(a,b,c)))

def Variacao_lista(a,b,c):
    '''Função que identifica a lista com a variação da sequencia; int, int, int --> float
    '''
    return list(range(a,b,c))

#main --- 2#
def main2():

    i = 0

    while i !=5:
        #opções para a escolha da operação que deseja fazer#
        print('digite(1) para area do trapezezio.')
        print('digite(2) para multiplicar os valores.')
        print('digite(3) para verificar a media desses valores.')
        print('digite(4) para somar a variação.')
        print('digite(5) para encerrar')

        #Entrada dos dados#
        i = int(input('digite aqui:\n'))

        #sequencia de condicionais relativos a entrada de dados i#
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
