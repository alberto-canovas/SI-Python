#!/usr/bin/python3

import sys
import subprocess



def main():
    argumentos=sys.argv[1:]
    limpiar_pantalla()
    #borrar_directorios_personales()
    if not es_argumento_correcto(argumentos):
        print('ERROR **Introduzca menos de 10 argumentos**')
        sys.exit()
    crear_directorios_personales()
    crear_directorio_alumno(argumentos)


def borrar_directorios_personales():
    subprocess.run(['rmdir','directorios_personales'])

def crear_directorios_personales():
    subprocess.run(['mkdir', 'directorios_personales'])


def crear_directorio_alumno(argumentos):
    subprocess.run(['cd', 'directorios_personales'])
    for argumento in argumentos:
        subprocess.run(['mk dir', {argumento}])


def es_argumento_correcto(argumentos):
    if len(argumentos)>10:
        return False
    return True























def limpiar_pantalla():
    subprocess.run('clear')

if __name__ == '__main__':
    main()