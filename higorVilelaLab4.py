import math

#1
def siga(tupla):       
    '''
    A função recebe uma tupla contendo o nome e as 3 notas da prova do aluno, retorna a media final
    e o resultado se aprovado ou reprovado;
    Sendo respectivamente nome (sting), nota 1, nota 2 e nota 3;
    tuple ---> tuple
    '''
    media_prova = math.floor((tupla[1]+tupla[2]+tupla[3])/3)
    if media_prova>=7:
        media_prova= (tupla[0],  media_prova, 'aprovado', 'parabéns!')

    elif 5 <= media_prova < 7:
         media_prova= (tupla[0],  media_prova, 'aprovado')

    elif media_prova<5:
        media_prova= (tupla[0], media_prova, 'reprovado')
        
    return media_prova

#2
def Siguino_china(ano_nasc):
    '''
    A função recebe o ano de nascimento e retorna o siguino chines pertencente;
    int ---> string
    '''
    ano= (ano_nasc)/12
    
    siguino =('macaco','galo','cão','porco','Rato','Boi','Tigre','Coelho','Dragão','Serpente','Cavalo','Carneiro')
    
    z= int((ano%1)*10)
    
    return siguino[z]


#3
def numero (numero):
    '''
    A função recebe um numero de telefone, verifica se é valido no Brasil e retorna o resultado da validação;
    string ---> string
    '''
    ddd= (numero[0:2])

    if len(numero)==10 or len(numero) ==11:
        numero=(ddd,numero[2:11])

    elif len (numero)<8 or len(numero)>11:
        numero=('','')

    return numero



#4
def formato_data(data):

    '''
     A função recebe uma string de 8 posições e retorna tres tipos de variações de formato de data
     (ddmmyyyy, yyyymmdd, mmddyyyy); string--->tuple
    '''
    dia= data[0:2]
    mes= data[2:4]
    ano=data[4:8]
    varia_data=(( dia + '/' + mes + '/' + ano), (ano +'/'+ mes +'/'+ dia) , (mes+'/'+dia+'/'+ano))

    if len(data)!=8:
        x= (( '' + '/' + '' + '/' + ''), ('' +'/'+ '' +'/'+ '') , (''+'/'+''+'/'+''))
             
    return varia_data
    
    
                                       
    
    


