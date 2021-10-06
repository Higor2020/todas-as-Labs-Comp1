
###cálculos algébricos###

#1#

##a##
def media(a,b,c):
    """
    calcula e retorna a média de [a,b,c] diferentes positivos e negativos;
    int,int,int ---> float
    """
    return (a+b+c)/3

##b##
def maxmed (a,b,c):
    """
    calcula a media de tres numeros aleatorios e subtrai o maior valor entre eles pela media;
    int,int,int ---> float
    
    """
    return ((a+b+c)/3) - max(a,b,c)

##c##
def minmed(a,b,c):
    """
    calcula a media de tres numeros aleatorios e subtrai o menor valor entre eles pela media;
    int,int,int ---> float
    """
    return ((a+b+c)/3) - min(a,b,c)

#2#

def delta(a,b,c):
    """
    calcula e retorna o delta de um polinomio de grau 2 ax2+bx+c ; onde, a= ax2 ,b=bx e c=c;
    int,int,int---> int
    """
    return (b**2)- 4*a*c

def raizdelta (a,b,c):
    """
    calcula a raiz quadrada da função 'delta'; onde, caso o delta < 0 não é uma função;
    int,int,int ---> float
    """
    return (delta(a,b,c))**(0.5)

def x_posit(a,b,c):
    """
    calcula os dados de entrada de ax2+bx+c; sendo a= ax2 ,b=bx e c=c e retorna a o x1 do polinomio;
    int,int,int ---> float
    """
    return (-b + raizdelta(a,b,c))/2*a

def x_negat(a,b,c):
    """
    calcula os dados de entrada de ax2+bx+c; sendo a= ax2 ,b=bx e c=c e retorna a o x2 do polinomio;
    int,int,int ---> float
    """
    return (-b - raizdelta(a,b,c))/2*a



#3#

def razao(a1,a2):
    """
    calcula e retorna a razão de uma PA, onde um dado numero da progressao(a1) é subtraido do seu sucessor (a2);
    float,float --> float
    """
    return a2 - a1

def quantt(a1,a2,an):
    """
    calcula e retorna a quantidade de termos de uma PA, onde, an=ultimo termo da PA, a1=primeito termo e a2= segundo termo;
    float,float --> float
    """
    return an/(razao(a1,a2))

def somapa(a1,a2,an):
    """
    calcula e retorna a soma do numero de termos de uma PA; onde, an=ultimo termo da PA, a1=primeito termo e a2= segundo termo;
    float,float --> float
    """
    return ((a1+an)*quantt (a1,a2,an))/2



###cálculos geométricos###

#4#

import math

#a
def dist_dpontos(x1,y1,x2,y2):
    """
    calcula e retorna a distancia entre dois pontos no R2; onde, x1 e y1= as coordenadas de umn ponto e
    x2 e y2= as coordenadas do outro ponto; int,int,int,int ---> float
    """
    return math.sqrt((x2-x1)**2 +(y2-y1)**2)

#b
def hipotenusa(a,b):
    """
    calcula a hipotenusa de um triangulo reto dado os catetos a e b; float,float -->float
    """
    return math.sqrt((a**2)+(b**2))

def perimet_triangulo(a,b):
    """
    calcula o perimetro do triangulo reto dado os catetos (a,b) e a hipotenusa; float, float---> float
    """
    return a+b+hipotenusa(a,b)

#c
def radiquad(a):
    """
    calcula a soma dos quadrados de seno e cosseno de um dado angulo(a); int--> float
    """
    return (math.cos(math.radians(a))**2) + (math.sin(math.radians(a))**2)

def sencosquad(a):
    """
    calcula a soma dos quadrados de seno e cosseno de um dado angulo(a)e eleva o resultado ao quadrado;
    int--> int
    """
    return math.sqrt(radiquad(a))

##5##
def area_circulo(r):
    """
    calcula e retorna a area do circulo(r);
    float-->float
    """
    return math.pi*(r**2)


def area_scircular(r,a=360):
    """
    calcula e retorna a area de um setor circular, onde r=raio do circulo e a=angulo do setor circular;
    caso a="" então a=360°; float, float ---> float
    """
    return ((a)*area_circulo(r))/360

###cálculos aplicados###

##1##
def num_bombons(a,b):
    """
    seja a=dinheiro de pedrinho e b=preço do bombon, a função calcula e retorna
    a quantidade de bombons que pedrinho pode comprar;
    float,float --> int
    
    """
    return math.floor(a/b)

##2##
def carros(x,y=5):
    """
    calcula e retorna a quantidade de veiculos necessários
    para transportar um determinado n° de pessoas(x).
    Caso a capacidade do transporte não for declarada no parametro(Y)
    sera considerado o padrão de 5 lugares;
    int,int ---> int
    """
    return math. ceil (x/y)

##3##
def max_bolos(a,b,c):
    """
    calcula e retorna o divisor comum entre as quantidades dos igredientes que
    é a quantidade maxima de bolos que podem ser feitos.
    onde, (a=xicaras farinha de trigo b=ovos c=colheres de sopa de leite);
    int,int,int --> int
    """
    return math.gcd(a,b,c)



    


