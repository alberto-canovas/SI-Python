import os

def main():
    try:
        limpiar_pantalla()
        crear_fecha(29,2,2024)
        crear_fecha(32,1,2024)
        crear_fecha(31,4,2024)
    except Exception as error:
        print(error)



def limpiar_pantalla():
    os.system('cls')




def crear_fecha(dia, mes, year):

    if mes < 1 or mes > 12:
        raise Exception ('El mes introducido es incorrecto.')

    if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        if dia < 1 or dia > 31:
            raise Exception ('El día introducido es incorrecto (31).')

    if mes == 2:
        if dia < 1 or dia > 28:
            raise Exception ('El día introducido es incorrecto(28).')

    if mes == 2 or 4 or 6 or 9 or 11:
        if dia < 1 or dia > 30:
            raise Exception ('El día introducido es incorrecto(30).')
        
    print(f'FECHA: {dia}/{mes}/{year}')




if __name__ == '__main__':
    main()