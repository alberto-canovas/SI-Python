#!/usr/bin/python3

import subprocess

USUARIOS= ['juan','cristina','maria','nicolas','fernando']

def main():
    limpiar_pantalla()
    crear_directorios(USUARIOS)

def crear_directorios(directorios):
    for directorio in directorios:
        resultado=subprocess.run(['mkdir',directorio], text=True, capture_output=True)
        if resultado.returncode == 0:
            print(f'Se ha creado con exito el directorio {directorio}')
        else:
            print(f'ERROR, no se ha creado el directorio {directorio}') 





















def limpiar_pantalla():
    subprocess.run('clear')

if __name__ == '__main__':
    main()
