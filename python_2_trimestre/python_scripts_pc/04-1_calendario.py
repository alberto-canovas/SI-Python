#!/usr/bin/python3
import subprocess
import sys






def main():
    limpiar_pantalla()


    argumentos = sys.argv[1:]
    if not son_argumentos_correctos(argumentos):
        print('El mes introducido no existe')
        sys.exit()
    mes = argumentos[0]
    mes = str(convertir_mes(mes))
    año = argumentos[1]
    mostrar_calendario(mes, año)








def son_argumentos_correctos(argumentos):
    if len(argumentos) != 2:
        return False
    mes_letra = sys.argv[1]
    mes = convertir_mes(mes_letra)
    if mes == None:
        return False
    año = sys.argv[2]
    if not año.isnumeric():
        return False
    return True
   


def limpiar_pantalla():
    subprocess.run('clear')


def mostrar_calendario(mes, año):
    subprocess.run(['cal', mes, año])


def convertir_mes(mes):
    match mes:
        case 'enero':
            return 1
        case 'febrero':
            return 2
        case 'marzo':
            return 3
        case 'abril':
            return 4
        case 'mayo':
            return 5
        case 'junio':
            return 6
        case 'julio':
            return 7
        case 'agosto':
            return 8
        case 'septiembre':
            return 9
        case 'octubre':
            return 10
        case 'noviembre':
            return 11
        case 'diciembre':
            return 12
        case _:
            return None




if __name__ == "__main__":
    main()
