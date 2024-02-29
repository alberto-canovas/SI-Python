#!/usr/bin/python3

import sys

def main():
    valores_linea_comandos = sys.argv
    print(valores_linea_comandos)
    argumentos = sys.argv[1:]
    print(argumentos)


    
if __name__ == '__main__':
    main()