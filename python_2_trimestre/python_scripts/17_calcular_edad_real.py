# Desarrolla un script que reciba como argumento por la linea de comandos el día de nacimiento
# en la forma 18/11/1998 y muestre por pantalla la edad del día de hoy (día en el que se ejecuta el script)

import subprocess,os,sys



def main():
    argumentos = sys.argv[1:]
    limpiar_pantalla()
    if not son_argumentos_correctos(argumentos):
        print('La fecha introducida no es correcta.')
        sys.exit()
    todo()
    

def mostrar_fecha_nacimiento():
    argumentos = sys.argv[1:]

    dia_nacimiento = argumentos[0].split('/') [0]
    mes_nacimiento = argumentos[0].split('/') [1]
    año_nacimiento = argumentos[0].split('/') [2]
    print(f'{dia_nacimiento}/{mes_nacimiento}/{año_nacimiento}')
    
def convertir_mes_numero(mes):
    match mes: # switch
        case 'Ene':
            return 1
        case 'Feb':
            return 2
        case 'Mar':
            return 3
        case 'Abr':
            return 4
        case 'May':
            return 5
        case 'Jun':
            return 6
        case 'Jul':
            return 7
        case 'Ago':
            return 8
        case 'Sep':
            return 9
        case 'Oct':
            return 10
        case 'Nov':
            return 11
        case 'Dic':
            return 12
        case _: # default
            return None

def obtener_fecha_actual():
    
    resultado = subprocess.run(['date'], text=True,capture_output=True)
    if resultado.returncode == 0:
        fecha_actual = resultado.stdout.strip()
        dia = fecha_actual.split(' ')[2]
        mes = fecha_actual.split(' ')[1]
        año = fecha_actual.split(' ')[5]
        
        print(f'FECHA ACTUAL: {dia}/{mes}/{año}')
    else:
        print('No se ha podido mostrar la fecha actual')

def calcular_edad():
    edad = año_nacimiento - año

    if mes_nacimiento > mes:
        if dia_nacimiento >= dia:
            return edad
    else:
        return edad-1

    

def todo():
    argumentos = sys.argv[1:]

    dia_nacimiento = argumentos[0].split('/') [0]
    mes_nacimiento = argumentos[0].split('/') [1]
    año_nacimiento = argumentos[0].split('/') [2]
    print(f'FECHA NACIMIENTO: {dia_nacimiento}/{mes_nacimiento}/{año_nacimiento}')



    resultado = subprocess.run(['date'], text=True,capture_output=True)
    if resultado.returncode == 0:
        fecha_actual = resultado.stdout.strip()
        dia = fecha_actual.split(' ')[2]
        mes = fecha_actual.split(' ')[1]
        año = fecha_actual.split(' ')[5]
        convertir_mes_numero(mes)
        print(f'FECHA ACTUAL: {dia}/{mes}/{año}')
    else:
        print('No se ha podido mostrar la fecha actual')


    edad = int (año) - int (año_nacimiento) 
    if int(mes_nacimiento) < convertir_mes_numero(mes):
        return print(f'La edad es {edad}')
    elif int(mes_nacimiento) == convertir_mes_numero(mes) and int(dia_nacimiento) <= int(dia):
        return print(f'La edad es {edad}')
    else:
        return print(f'La edad es {edad-1}')


def son_argumentos_correctos(argumentos):
    argumentos = sys.argv[1:]
    dia_nacimiento = argumentos[0].split('/') [0]
    mes_nacimiento = argumentos[0].split('/') [1]
    año_nacimiento = argumentos[0].split('/') [2]
    if len(argumentos)!= 1:
        return False
    if not dia_nacimiento.isnumeric():
        return False
    if int(dia_nacimiento) < 1:
        return False
    if int(mes_nacimiento)== 1 or 3 or 5 or 7 or 8 or 10 or 12 and int(dia_nacimiento) > 31:
        return False
    if int(mes_nacimiento)== 2 and int(dia_nacimiento) > 28:
        return False
    if int(mes_nacimiento)== 4 or 6 or 9 or 11 and dia_nacimiento > 30:
        return False
    if not mes_nacimiento.isnumeric() or int(mes_nacimiento):
        return False
    if int(mes_nacimiento) < 1 or int(mes_nacimiento) > 12:
        return False
    if not año_nacimiento.isnumeric():
        return False 
    return True


def limpiar_pantalla():
    subprocess.run('clear')

if __name__ == '__main__':
    main()
