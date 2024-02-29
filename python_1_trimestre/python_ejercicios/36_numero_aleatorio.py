import os
os.system('cls')
import random

# numeros=[]
# pares=[]
# impares=[]

# for i in range(0,1000):
#     mil=(random.randint(1,1000))
#     numeros.append(mil)

#     if mil %2==0:
#         pares.append(mil)
#     else:
#         impares.append(mil)

# print() 
# print(len(pares))
# print(len(impares))


def generar_numeros_aleatorios(cantidad):
    numeros=[]

    for i in range (cantidad):
    numeros=(random.randint(1,cantidad))




def devolver_pares(numeros):
    pares=[]
    for numero in numeros:
        if es_par(numero):
            pares.append(numero)
    return pares



def es_par(numero):
    if numero%2==0:
        return True
    else:
        return False
    
def filtrar_impares(numeros):
    impares=[]
    for numero in numeros:
        if not es_par(numero):
            impares.append(numero)
    return impares

    