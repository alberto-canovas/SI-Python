import os


def limpiar_pantalla():
    os.system('cls')





def main():
    limpiar_pantalla()
    try:
        print(dividir(10, 5))
        print(dividir(20, 5))
        print(dividir(10, 0))
    except Exception as error:
        print(f'El problema es: {error}')


    


def dividir( dividendo, divisor ):
    if divisor == 0:
        raise Exception('No se puede dividir entre cero.')
    
    resultado = dividendo / divisor
    return resultado


if __name__ == '__main__':
    main()
