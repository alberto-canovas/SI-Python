#!/usr/bin/python3

import subprocess
import sys

def main():
    
    limpiar_pantalla()

    while True:
        mostrar_menu()

        opcion=pedir_opcion()
        match opcion:
            case 1:
                mostrar_fecha()
            case 2:
                mostrar_quien_soy()
            case 3:
                mostrar_quien_esta_conectado()
            case 4:
                mostrar_calendario()
            case 5:
                ...
            case 6:
                cerrar_aplicacion()


        # if opcion ==1:
        #     mostrar_fecha()
        # elif opcion ==2:
        #     mostrar_quien_soy()
        # elif opcion==3:
        #     mostrar_quien_esta_conectado()
        # elif opcion==4:
        #     mostrar_calendario()
        # elif opcion==5:
        #     ...
        # elif opcion==6:
        #     cerrar_aplicacion()

    


def pedir_opcion() -> int:
    while True:
        respuesta = input("Introduzca una opción del menú: ")

        if respuesta.isnumeric():
            opcion = int(respuesta)

            if opcion < 1 or opcion > 6:
                print("Debe introducir una opción permitida.")
            else:
                return opcion
                
        else:
            print("Debe introducir un número.")


def mostrar_fecha():
    subprocess.run(['date','+"%d/%m/%Y"'])

def mostrar_quien_soy():
    subprocess.run("whoami")

def mostrar_quien_esta_conectado():
    subprocess.run("who")

def mostrar_calendario():
    subprocess.run("cal")

def limpiar_pantalla():
    subprocess.run("clear")

def cerrar_aplicacion():
    print("Saliendo...")
    sys.exit
def cambiar_contraseña():
    subprocess.run("passwd")

def mostrar_menu():
    print("\n--------------- Menú --------------")
    print("\t1) Mostrar fecha.")
    print("\t2) Mostrar quién soy.")
    print("\t3) Mostrar quién está conectado.")
    print("\t4) Mostrar calendario.")
    print("\t5) Mostrar la contraseña.")
    print("\t6) Cerrar el script.")


if __name__ == "__main__":
    main()