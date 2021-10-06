#1
def absoluto(x):
    ''' A função retorna o valor absoluto de um dado número x de entrada;
        onde x é um numero real; float --> float
    '''
    if x>0:
        return x
    else:
        return (-1)*x
     
#2
def Num_raizes (a,b,c):
    '''
        A função retorna a quantidade de raizes existentes de um polinomio de grau 2;
        onde, ax 2 =a , bx=b e c=c sao os dados de entrada respectivamente;
        float,float,float --> float 
    '''
    msg =''
    if ((b**2)- 4*a*c > 0):
        msg = '2 raizes'

    elif ((b**2)- 4*a*c == 0):
        msg = '1 raiz'

    else:
        msg = '0 raizes'

    return msg


#3
def repit_texto (texto,repetiçoes):
    '''
        A função retorna uma cadeia de caracteres n vezes;
        string, int --> string
    '''
    return str(texto)*repetiçoes


#4
def data (dia, mes, ano):
    '''
        A função retorna uma data com os dados de entrada dia, mes e ano respectivament;
        int,int,int --> int
    '''
    return str(dia)+ '/' + str(mes)+'/'+ str(ano)


#5
def comport_func(y):
    '''
        A função retorna os casos de teste da questão 5 e y como entrada de dados;
        float--> float
    '''
    if y>=0 and y<=2:
        return 'x'
    elif y>=2 and y<=3.5:
        return 2
    elif y>=3.5 and y<=5:
        return 3
    elif y>=5:
        return (y**2)-(10*y)+28
    else:
        return 'não pertence a função'



#6
#a
def desc_inss(salario_bruto):
    '''
        calcula o desconto do inss no salario bruto; float --> float
    '''
    
    if salario_bruto <=2000:
        return (salario_bruto)*0.06

    elif 2000 < salario_bruto <= 3000:
        return (salario_bruto)*0.08
        
    else:      
        return salario_bruto * 0.10


#b
def desc_ir(salario_bruto):
    '''
        calcula o desconto do IR no salario bruto; float--> float
    '''
    
    if salario_bruto <=2500:
        return (salario_bruto)*0.11

    elif 2500 < salario_bruto <= 5000:
        return (salario_bruto)*0.15
        
    else:      
        return salario_bruto * 0.22


#c
def salario_liquido(salario_bruto):
    '''
        A função retorna o salario bruto com os descontos do INSS e do IR juntos; float--> float
    '''
    return salario_bruto - (desc_inss(salario_bruto) + desc_ir(salario_bruto))
