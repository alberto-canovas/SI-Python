import os
os.system('cls')

Dos_hombres_y_un_destino={
    'Autor': 'David Bustamante',
    'Título':'Dos hombres con un mismo destino',
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
    print('{:35} {:15} {:20} {:20} {:5}'.format('TÍTULO','AUTOR','AÑO DE LANZAMIENTO', 'GÉNERO','VALORACIÓN'))
    print('-'*115)
    for cancion in canciones:
        print(f'{cancion['Título']:35}{cancion['Autor']:20}{cancion['Año de lanzamiento']:20}{cancion['Género']:20}{cancion['Valoración']:5}')

mostrar_canciones(canciones)


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
    'Autor': input('Dime un Autor '),
    'Título':input('Dime un Título '),
    'Año de lanzamiento':int(input('Dime un Año de lanzamiento ')),
    'Género':input('Dime un Género '),
    'Valoración':int(input('Dime un Valoración ')),
    }
    canciones.append(cancion_nueva)




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
        case 6:
            print('Saliendo...')
            break
        case 4:
            cancion_nueva=agregar_cancion(canciones)
            canciones.append(cancion_nueva)
        

    
      

