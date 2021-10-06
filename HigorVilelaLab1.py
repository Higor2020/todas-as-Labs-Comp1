"""calculo geométrico"""

def area_retangulo(b,h):
    """ retorna a área de um retângulo, onde (base retângulo,altura retângulo) """
    return b*h

def area_superfecie_cubo(c):
    """ retorna a area da superficie de um cubo, onde c = aresta do cubo"""
    return 6*(c**2)

def area_coroa_circular(R,r):    
    """a função retorna a area da coroa circular, onde as entradas são respectivamente
(raio maior,  raio menor)"""
    return 3.14*((R**2)-(r**2))


""" Calculos Algébricos """

def media(x,y):
    """ a função retorna a media de dois numeros reais inseridos"""
    return (x+y)/2

def funç_seg_grau(a,b,c,x):
    """ a função retorna o calculo de um polinomio ax² +bx +c, onde os dados de entrada são respectivamente (a,b,c,x)"""
    return (a*(x**2)) + (b*x) + c


def media_ponderada(a,b):
    """ a função retorna a media ponderada de dois numeros reais, onde respectivamente (a*2,b*4)""" 
    return ((a*2)+(b*4))/6

def erro_pg(q,n,a):
    """ onde temos respectivamente (razão, numero de termos, primeiro termo da progressão)"""
    return (1/(1-q))-(a*((q**n)-1)/(q-1))



""" calculo aplicado"""

def taxa_garçon(x):
    """ Essa função retorna o valor da gorgeta de 15% do garçom sobre o valor gasto()"""
    return x*(0.15)

def taxa_atendimento(x,y):
    """ a função retorna a taxa de serviço do garçon, onde os dados são respectivamente ( valor conta, taxa serviço),
taxa serviço --> numeros naturais positivos não nulos"""
    return x*(y/100)

def saldo_final(x,y,z):
    """ a função retorna o saldo ao final do periodo, onde os dados são respectivamente ( saldo inicial, juros, meses)"""
    return x*(1+(y*z))

def arrasta_barco(lr,vb,vc):
    """ onde temos respectivamente ( largura do rio, velocidade do barco perpendicular a corenteza, velocidade correnteza)"""
    return (lr/vb)*vc 


def coroa (x,y):
    return  (3.14 * x**2) - (3.14 * y**2)

    






        

        
    
    


    
