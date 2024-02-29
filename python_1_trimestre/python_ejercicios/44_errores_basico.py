import os
os.system('cls')

# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
    
#OPERADOR TERNARIO    
# def es_par(numero):
#     return True if numero % 2 == 0 else False

#SIN NADA PQ LA FUNCION DEVUELVE UN BOLEANO
def es_par(numero):
    return numero % 2 == 0 

try:
    numero=int(input('Dame un número: '))
    if es_par(numero):
        print(f'El número {numero} es par.')
    else:
        print(f'El número {numero} es impar.')
except Exception:
    print('ERROR: Debes introducir un número.') 
       
# print(es_par(8))
# print(es_par(-8555))