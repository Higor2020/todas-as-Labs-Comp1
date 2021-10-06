#1#
def multiplica_matriz(matriz,numero):
    '''A função recebe uma matriz e um numero real como parametros de entrada,
       esse numero multiplicará cada elemento matricial e retornará o resultado da matriz multiplicada;
       list, float --> list
       
    '''
    i= 0
    lst =[]
    
    for elem in matriz:
        lst1 = []
        for elem in matriz[i]:
            list.append(lst1,numero*elem)
        list.append(lst, lst1)
        i+=1
    return lst

    
        
    
#3# 
def quem_ligou(telefone, agenda):
    '''A função recebe um numero de telefone e a agenda do contatinhosapp,
        e retorna as informações correspondentes ao portador do numero;
        str,list --> list
    '''
    contatinhos = []
    i = 0
    for elem in agenda:
        for elem in agenda[i]:
            if elem == telefone:
                list.append(contatinhos, agenda[i])
        i+=1
    return contatinhos

            
