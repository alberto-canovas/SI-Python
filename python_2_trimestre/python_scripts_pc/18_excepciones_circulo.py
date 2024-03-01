import subprocess,os,math,sys

def main():
    argumentos = sys.argv[1:]
    limpiar_pantalla()
    try:
        son_argumentos_correcto(argumentos)
        calcular_area_circulo(4)
        calcular_perimetro_circulo(4)
        calcular_area_circulo(5)
        calcular_perimetro_circulo(-3)
    except Exception as error:
        print(error)



def son_argumentos_correcto(argumentos):
    if len(argumentos)!=1:
        raise Exception('El número de argumentos es erróneo')
    if int(argumentos[0])<0:
        raise Exception('El número tiene que ser positivo')
    if not argumentos.isnumeric:
        raise Exception('El argumento debe de ser un número')
    return True 

def calcular_area_circulo(radio):
    # if not radio.isnumeric():
    #     raise Exception('El radio debe ser un número')
    if radio<0:
        raise Exception('El radio tiene que ser positivo')
    area = math.pi*(radio*radio)
    round(area,2)
    print(f'El area es {round(area,2)}')

def calcular_perimetro_circulo(radio):
    # if not radio.isnumeric():
    #     raise Exception('El radio debe ser un número')
    if radio<0:
        raise Exception('El radio tiene que ser positivo')
    perimetro = 2*math.pi*radio
    round(perimetro,2)
    print(f'El perimetro es {round(perimetro,2)}')

def limpiar_pantalla():
    subprocess.run('clear')


if __name__ == '__main__':
    main()