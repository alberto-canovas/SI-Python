#!/usr/bin/python3

import sys
import subprocess

def main():
    argumentos=sys.argv[1:]
    limpiar_pantalla()
    if not es_argumento_correcto(argumentos):
        print('ERROR Introduzca un número entero')
        sys.exit()

    mostrar_y_calcular_tabla(argumentos)


def limpiar_pantalla():
    subprocess.run('clear')



def es_argumento_correcto(argumentos):
    argumentos=sys.argv[1:]
    base=argumentos[0]
    if len(argumentos)!=1:
        return False
    if not base.isnumeric():
        return False
    return True


def mostrar_y_calcular_tabla(argumentos):
    resultado=0
    for i in range(0,10):
        resultado=i*argumentos[0] 
        print(f"\n{i} x {argumentos[0]} = {resultado}")
        





if __name__ == '__main__':
    main()