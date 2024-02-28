#!/usr/bin/python3

import subprocess
import sys

comunidades=['andalucia', 'aragon', 'islas-baleares', 'canarias', 'cantabria', 'castilla-la-mancha', 
                'castilla-y-leon', 'catalunya', 'madrid', 'navarra', 'comunidad-valenciana', 'extremadura', 
                'galicia', 'pais-vasco', 'asturias', 'murcia', 'rioja']

def main():
    argumentos=sys.argv[1:]
    limpiar_pantalla()
    
    if len(argumentos)!=1:
        print('ERROR introduce una cadena de texto')
        sys.exit()

    if es_comunidad_correcto(argumentos):
        print('Comunidad correcta')
        sys.exit()
    
    if not es_comunidad_correcto(argumentos):
        print('Comunidad errónea')
        sys.exit()

def es_comunidad_correcto(argumentos):

    comunidad = argumentos[0]
    if comunidad in comunidades:
        return True
        

def limpiar_pantalla():
    subprocess.run('clear')



if __name__ == '__main__':
    main()








  