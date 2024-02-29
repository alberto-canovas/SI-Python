import os
os.system('cls')
import math
math.sqrt(9)


def calcular_raiz_x1(a,b,c): #a, b y c son los parametros q se necesitan para q se cumpla la funcion

#** se utiliza para elevar un exponente

    x1=(-b + math.sqrt(b**2-4*a*c))/2*a 
    return x1
def calcular_raiz_x2(a,b,c):

    x2=(-b - math.sqrt(b**2-4*a*c))/2*a
    return x2


a=int(input('Dime un valor a--> '))
b=int(input('Dime un valor b--> '))
c=int(input('Dime un valor c--> '))

x1=calcular_raiz_x1(a,b,c)
x2=calcular_raiz_x2(a,b,c)
print(f'x1 es = {x1}')
print(f'x2 es = {x2}')
