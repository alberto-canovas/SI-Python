#!/usr/bin/python3

import subprocess
import sys



primero=['empresa','ingles','fol','base de datos','sistemas informáticos','programación','entornos de desarrollo']

segundo=['lenguajes-de-marca','desarrollo web entorno-clliente','desarrollo web entorno-servidor','diseño de interfaces','despliegue de aplicaciones']


def main():
    argumentos=sys.argv[1:]
    limpiar_pantalla()

    if not son_argumentos_correctos(argumentos):
        return True
    
        
    
    if  son_argumentos_correctos(argumentos):
        print('Escribe solo un argumento')
        sys.exit()




def limpiar_pantalla():
    subprocess.run('clear')



def son_argumentos_correctos(argumentos):
    curso=argumentos[0]

    if len(curso)!=1:
        return False
    
    if curso==None:
        print(primero)
        print(segundo)
        return True
    
    if curso== 1:
        print(primero)
        return True
    
    if curso== 2:
        print(segundo)
        return True
    
    

    




























if __name__=='__main__':
    main()

