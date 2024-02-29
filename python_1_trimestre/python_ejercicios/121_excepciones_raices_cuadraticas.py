import os

def limpiar_pantalla():
    os.system('cls')


def main():
    try:
        limpiar_pantalla()
        calcular_raices_cuadradas(1,2,3)
    except Exception as error:
        print(error)


def calcular_raices_cuadradas(a,b,c):
    radicando = b * b - 4 * a * c
    if radicando < 0:
        raise Exception ('La raíz cuadrada no puede ser negativa.')
    else:
        raiz_positiva = 3
        raiz_negativa = 5
        return raiz_positiva, raiz_negativa
    

if __name__ == '__main__':
    main()

