import os
os.system('cls')

Dos_hombres_y_un_destino={
    'Autor': 'David Bustamante',
    'Título':'Dos hombres y un destino',
    'Año de lanzamiento':'2002',
    'Género':'Pop',
    'Valoración':1
    }

Waka_Waka={
    'Autor': 'Shakira',
    'Título':'Waka Waka',
    'Año de lanzamiento':'2010',
    'Género':'Pop',
    'Valoración':2
}

The_Monster={
    'Autor': 'Eminen',
    'Título':'The Monster',
    'Año de lanzamiento':'2013',
    'Género':'Rap',
    'Valoración':3,
}

Fiesta_pagana={
    'Autor': 'Mago de Oz',
    'Título':'Fiesta Pagana',
    'Año de lanzamiento':'2000',
    'Género':'Rock',
    'Valoración':4,
}

Candy_shop={
    'Autor': '50 cent',
    'Título':'Candy shop',
    'Año de lanzamiento':'2005',
    'Género':'Rap',
    'Valoración':5,
}

Sweet_child_o_mine={
    'Autor': 'Guns n Roses',
    'Título':'Sweet child o mine',
    'Año de lanzamiento':'1987',
    'Género':'Rock',
    'Valoración':6,
}

Thriller={
    'Autor': 'Michael Jackson',
    'Título':'Thriller',
    'Año de lanzamiento':'1982',
    'Género':'Pop',
    'Valoración':7,
}

Billie_jean={
    'Autor': 'Michael Jackson',
    'Título':'Billie Jean',
    'Año de lanzamiento':'1982',
    'Género':'Pop',
    'Valoración':8,
}

Ave_maria={
    'Autor': 'David Bisbal',
    'Título':'Ave María',
    'Año de lanzamiento':'2002',
    'Género':'Pop',
    'Valoración':9,
}

Rap_god={
    'Autor': 'Eminem',
    'Título':'Rap God',
    'Año de lanzamiento':'2013',
    'Género':'Rap',
    'Valoración':10,
}

canciones=[Dos_hombres_y_un_destino,Waka_Waka,The_Monster,Fiesta_pagana,Candy_shop,
Sweet_child_o_mine,Thriller,Billie_jean,Ave_maria,Rap_god]


def mostrar_canciones(canciones):
    print('{:35} {:30} {:30} {:20} {:5}'.format('TÍTULO','AUTOR','AÑO DE LANZAMIENTO', 'GÉNERO','VALORACIÓN'))
    print('-'*130)
    for cancion in canciones:
        print('{:35} {:30} {:30} {:20} {:5}'.format(cancion['Título'],cancion['Autor'],cancion['Año de lanzamiento'],cancion['Género'],cancion['Valoración']))



# def mostrar_cinco_canciones_mas_valoradas(canciones):
#        canciones_mas_valoradas=[]
#        valoracion_max=-10
#        for cancion in canciones:
#             if cancion>valoracion_max:
#                 canciontop1=canciones_mas_valoradas.append(cancion)
#                 del canciones(canciontop1)
#             return canciones_mas_valoradas
       
#print(mostrar_cinco_canciones_mas_valoradas(canciones))


def agregar_cancion(canciones):
    cancion_nueva={
    'Autor': input('Dime un Autor: ').capitalize(),
    'Título':input('Dime un Título: ').capitalize(),
    'Año de lanzamiento':input('Dime un Año de lanzamiento: '),
    'Género':input('Dime un Género: ').capitalize(),
    'Valoración':int(input('Dime un Valoración: ')),
    }
    return cancion_nueva

def eliminar_cancion(canciones):
    i=0

    print('{:35}{:20}'.format('Título','Autor'))
    print('-'*50)

    for cancion in canciones:
        i+=1
        print(f'{i}.{cancion["Título"]:35}{cancion["Autor"]:20}')
    print('')
    opcion=int(input('Selecciona una canción: '))

    if 1<= opcion <=i:
        del canciones[opcion-1]
        print('')
        print('Canción eliminada')
    else:
        print('')
        print('Opción no válida')

def ordenar_canciones_por_genero(canciones):
    canciones_ordenadas=sorted(canciones, key=lambda x: x['Género'])
    return canciones_ordenadas

canciones_ordenadas=ordenar_canciones_por_genero(canciones)

def mostrar_canciones_ordenadas(canciones_ordenadas):
    print('{:40}{:20}'.format('Título','Género'))
    print('-'*50)
    for cancion in canciones_ordenadas:
        print(f'{cancion["Título"]:40}{cancion["Género"]:20} ')
    print('')




while True:
    print('             MENÚ DE USUARIO')
    print('---------------------------------------------')
    print('1. Mostrar todas las canciones.')
    print('2. Mostrar las cinco canciones más valoradas.')
    print('3. Mostrar las canciones ordenadas por género.')
    print('4. Añadir una nueva canción.')
    print('5. Eliminar una canción.')
    print('6. Salir de la aplicación.')
    print('')
    opcion=int(input('Seleccione una opción: '))
    print('')
    match opcion:
        case 1:
            mostrar_canciones(canciones)
        case 2:
            pass
        case 3:
            mostrar_canciones_ordenadas(canciones_ordenadas)
        case 4:
            cancion_nueva=agregar_cancion(canciones)
            canciones.append(cancion_nueva)
        case 5:
            eliminar_cancion(canciones)
        case 6:
            print('Saliendo...')
            break