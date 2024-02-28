#!/usr/bin/python3

import subprocess
import sys

subprocess.run(['cp','plantilla',''])




def main():
    argumentos=sys.argv[1:]
    limpiar_pantalla()

    if not son_argumentos_correctos(argumentos):
        print('Los argumentos son incorrectos.')
    else:
        numero_copias=int(argumentos[0])
        fichero=argumentos[1]
        nombre_copias=argumentos[2]
        copiar_ficheros(numero_copias,fichero,nombre_copias)
    
    



def son_argumentos_correctos(argumentos):
    
    if len(argumentos)!=3:
        print('ERROR introduce 3 argumentos')
        return False
    
    numero_copias=argumentos[0]
    if not numero_copias.isnumeric():
        print('ERROR inserte un número')
        return False
    
    fichero=argumentos[1]
    if fichero == None:
        return False
    
    nombre_copias=argumentos[2]
    if nombre_copias == None:
        return False
    
    return True


def copiar_ficheros(numero_copias,fichero,nombre_copias):
    
    for i in range(1,numero_copias+1):
        if i<10:
            resultado=subprocess.run(['cp',fichero,f'{nombre_copias}0{i}'])
        else:
            resultado=subprocess.run(['cp',fichero,f'{nombre_copias}{i}'])
        if resultado.returncode!=0:
            print('Ha habido un problema durante la copia.')
            break
        



def limpiar_pantalla():
    subprocess.run('clear')









if __name__=='__main__':
    main()

