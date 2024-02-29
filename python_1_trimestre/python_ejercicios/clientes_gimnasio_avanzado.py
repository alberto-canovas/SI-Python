import os
os.system('cls')


clientes_gimnasio_diccionario = [
    {'nombre': 'Juan','genero': 'M','altura': 182,'masa' :92},
    {'nombre': 'Alicia','genero': 'F','altura': 157,'masa': 52},
    {'nombre': 'Manuel','genero': 'M','altura': 171,'masa': 75},
    {'nombre': 'Loli','genero': 'F','altura': 160,'masa' :60},
    {'nombre': 'Pepe','genero': 'M','altura': 199,'masa' :70},
    {'nombre': 'Paco','genero': 'M','altura': 178,'masa' :79},
    {'nombre': 'Manolo','genero': 'M','altura': 175,'masa': 80},
    {'nombre': 'Pedro','genero': 'M','altura': 195,'masa': 90},
    {'nombre': 'Maria','genero': 'F','altura': 150,'masa': 50},
    {'nombre': 'Raquel','genero': 'F','altura': 155,'masa': 55},
]


def obtener_nombre_mas_alta(clientes):
    altura_max=0
    nombre_alto=''

    for cliente in clientes:
        nombre = cliente['nombre']
        altura = cliente['altura']
        if altura>altura_max:
            nombre_alto=nombre
            altura_max=altura
    return nombre_alto

print(obtener_nombre_mas_alta(clientes_gimnasio_diccionario))



