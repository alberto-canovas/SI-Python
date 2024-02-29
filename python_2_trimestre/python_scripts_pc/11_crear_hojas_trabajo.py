#!/usr/bin/python3

import sys
import subprocess


def main():
    argumentos=sys.argv[1:]
    limpiar_pantalla()



def limpiar_pantalla():
    subprocess.run('clear')


def es_argumento_correcto(argumentos):
    if argumentos!=1:
        return False

def obtener_dias_mes(argumentos):
    dias=0
    match argumentos:
        case 'enero':
            return 31
        case 'febrero':
            return 28
        case 'marzo':
            return 31
        case 'abril':
            return 30
        case 'mayo':
            return 31
        case 'junio':
            return 30
        case 'julio':
            return 31
        case 'agosto':
            return 31
        case 'septiembre':
            return 30
        case 'octubre':
            return 31
        case 'noviembre':
            return 30
        case 'diciembre':
            return 31
        case _: # default
            return None


if __name__ == '__main__':
    main()