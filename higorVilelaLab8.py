#1
def elementosNoiteravel(iteravel, elem):
    ''' A função recebe como dado de entrada um iteravel e um potencial elemento,
        faz uma varredura no primeiro parametro e retorna a quantidade de vezes que o elemento aparece no iteravel;
        iteravel, elemento --> int
    '''
    soma = 0
    
    for i in range(len(iteravel)):
        if elem == iteravel[i]:
            soma = soma + 1

        i+=1
        

    return soma

#2
def elementosRangeNoiteravel(iteravel, elem, ini, fim):
    '''A função recebe como parametro de entrada um iteravel, um elemento, um inteiro indicando o inicio do range e um inteiro indicando o fim.
        A função faz o mesmo processo de elementosNoiteravel, mas agora dentro de um range espefico no iteravel,
        caso o elemento não for encontrado o contador retornara 0; iteravel, elemento, int,int --> int
    '''
    contador = 0
    for i in range(ini, fim):
        if iteravel[i] == elem:
            contador+=1

    return contador

#3
def atualiza_mascara(palavra, lista, letra):
    '''A função recebe como parametro de entrada uma palavra, a mascara da palavra e uma letra.
        A função fará uma varredura na palavra em busca da letra, se for encontrada,
        a mascara revelará as posições do caractere simulando um jogo da forca; str, list, str --> list
    '''
    i= 0 
    for elem in range(len(palavra)):    
        if letra == palavra[i]:
            lista[i] = letra
        i+=1
    return lista



    

    


