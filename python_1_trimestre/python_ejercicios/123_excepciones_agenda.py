import os


agenda = [
    {'id': '1654-7354', 'nombre': 'Pedro López'},
    {'id': '1651-5214', 'nombre': 'Paco Luis'},
    {'id': '8579-6324', 'nombre': 'Jose Luis'},
    {'id': '1032-1543', 'nombre': 'Natalia Nadua'},
]


def añadir_contacto(id,nombre):
    if es_identificador_repetido(id):
        raise Exception('El id ya existe.')

    agenda.append({'id': id, 'nombre': nombre})


def limpiar_pantalla():
    os.system('cls')


def es_identificador_repetido():
    ...



def main():
    limpiar_pantalla()
    añadir_contacto('1654-7354','Maria Coronado')
    print(agenda)






if __name__ == '__main__':
    main()
