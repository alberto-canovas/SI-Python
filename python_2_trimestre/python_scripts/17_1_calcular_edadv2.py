

import subprocess,os,sys



def main():
    limpiar_pantalla()
    argumentos = sys.argv[1:]
    try:
        fecha_nacimiento = extraer_fecha_nacimiento(argumentos)
    except Exception as error:
        print(error)

    

    
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
    if resultado.returncode != 0:
        raise Exception('Ha habido un problema con el comando date.')
    else:
        print('No se ha podido mostrar la fecha actual')
        
    fecha_actual = resultado.stdout.strip()
    dia = fecha_actual.split(' ')[2]
    mes = convertir_mes_numero(fecha_actual.split(' ')[1])
    año = fecha_actual.split(' ')[5]

    print(f'FECHA ACTUAL: {dia}/{mes}/{año}')

def calcular_edad(fecha_nacimiento,fecha_actual):

    dia = int(fecha_actual[0].split('/') [0])
    mes = int(fecha_actual[0].split('/') [1])
    año = int(fecha_actual[0].split('/') [2])


    edad = año - año_nacimiento 
    if mes_nacimiento < convertir_mes_numero(mes):
        return print(f'La edad es {edad}')
    elif mes_nacimiento == convertir_mes_numero(mes) and dia_nacimiento <= dia:
        return print(f'La edad es {edad}')
    else:
        return print(f'La edad es {edad-1}')
    

def extraer_fecha_nacimiento(argumentos):
    if len(argumentos) != 1:
        raise Exception('El número de argumentos es erróneo.')
    
    fecha_troceada = argumentos[0].split('/')
    
    if len(fecha_troceada)!=3:
        raise Exception ('La fecha tiene un número de partes incorrecto')
    
    for item in fecha_troceada:
        if not item.isnumeric():
            raise Exception ('La fecha inlcuye un elemento no numérico.')

    fecha_nacimiento = argumentos [0]
    dia_nacimiento = int(fecha_nacimiento[0].split('/') [0])
    mes_nacimiento = int(fecha_nacimiento[0].split('/') [1])
    año_nacimiento = int(fecha_nacimiento[0].split('/') [2])    

def limpiar_pantalla():
    subprocess.run('clear')

if __name__ == '__main__':
    main()
