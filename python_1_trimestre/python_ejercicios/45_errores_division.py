import os
os.system('cls')

def dividir(dividendo,divisor):
    if divisor == 0:
        #print('ERROR')
        # return 0
        # return False
        #return None esta es la mejor opcion
        raise Exception('No se puede dividir entre 0.')
    else:
        cociente = dividendo / divisor
        return cociente

# print(dividir(8,2))
# print(dividir(8,0))

try:
     
     print(dividir(8,2))
     print(dividir(8,0))
except Exception as error:
     print(f'ERROR: {error}')


