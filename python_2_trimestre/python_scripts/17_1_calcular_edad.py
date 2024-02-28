

import subprocess,os,sys



def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    if es_argumento_correcto(argumentos):
        print('bueno')
    else:
        print('malo')
    fecha_nacimiento = argumentos[0]
    fecha_actual = obtener_fecha_actual()
    print(calcular_edad(fecha_nacimiento,fecha_actual))
    

    
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
            mes = convertir_mes_numero(fecha_actual.split(' ')[1])
            año = fecha_actual.split(' ')[5]

            print(f'FECHA ACTUAL: {dia}/{mes}/{año}')
    else:
        print('No se ha podido mostrar la fecha actual')

def calcular_edad(fecha_nacimiento,fecha_actual):

    dia_nacimiento = fecha_nacimiento[0].split('/') [0]
    mes_nacimiento = fecha_nacimiento[0].split('/') [1]
    año_nacimiento = fecha_nacimiento[0].split('/') [2]

    print(f'FECHA NACIMIENTO: {dia_nacimiento}/{mes_nacimiento}/{año_nacimiento}')

    dia = fecha_actual[0].split('/') [0]
    mes = fecha_actual[0].split('/') [1]
    año = fecha_actual[0].split('/') [2]


    edad = int (año) - int (año_nacimiento) 
    if int(mes_nacimiento) < convertir_mes_numero(mes):
        return print(f'La edad es {edad}')
    elif int(mes_nacimiento) == convertir_mes_numero(mes) and int(dia_nacimiento) <= int(dia):
        return print(f'La edad es {edad}')
    else:
        return print(f'La edad es {edad-1}')
    

def es_argumento_correcto(argumentos):
    if len(argumentos) != 1:
        return False
    
    fecha_troceada = argumentos[0].split('/')
    print(fecha_troceada)
    if len(fecha_troceada)!=3:
        return False
    
    for item in fecha_troceada:
        if not item.isnumeric():
            return False
         
    return True
    

def limpiar_pantalla():
    subprocess.run('clear')

if __name__ == '__main__':
    main()
