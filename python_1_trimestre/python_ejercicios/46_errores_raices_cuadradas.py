import os
os.system('cls')
import math

# a=int(input('Dime la a: '))
# b=int(input('Dime la b: '))
# c=int(input('Dime la c: '))

def calcular_raiz_negativa(a,b,c):
    radicando=(b**2-4*a*c)
    x1=(- b + math.sqrt(radicando)) /(2*a)    
    if a ==0:
        raise Exception ('No se puede dividir entre 0.')
    elif radicando<0:
        raise Exception('La raiz cuadrada es negativa.')
    else:
        return x1

def calcular_raiz_positiva(a,b,c):
    radicando=(b**2-4*a*c)
    x2=(- b + math.sqrt(radicando)) /(2*a)
    if a ==0:
        raise Exception ('No se puede dividir entre 0.')
    elif radicando<0:
        raise Exception('La raiz cuadrada es negativa.')
    else:
        return x2

try:
    print(calcular_raiz_negativa(64,80,25))
    # print(calcular_raiz_positiva(64,2,25))
    # print(calcular_raiz_positiva(0,80,25))

except Exception as error:
    print(f'ERROR: {error}')
