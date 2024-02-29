import os
os.system('cls')

clientes_gimnasio = [
    ['Juan', 'M', 182, 92],
    ['Alicia', 'F', 157, 52],
    ['Manuel', 'M', 171, 75],
    ['Loli', 'F', 160, 60],
    ['Pepe', 'M', 199, 70],
    ['Paco', 'M', 178, 79],
    ['Manolo', 'M', 175, 80],
    ['Pedro', 'M', 195, 90],
    ['Maria', 'F', 150, 50],
    ['Raquel', 'F', 155, 55],
    ]
print(len(clientes_gimnasio))

#Crea una función que devuelva el nombre de la persona más alta.

def obtener_nombre_persona_mas_alta(clientes):

    nombre_masalto=''
    altura_maxima=0
    for cliente in clientes:
        nombre=cliente[0]
        altura=cliente[2]
        if altura > altura_maxima:
            nombre_masalto=nombre
            altura_maxima=altura
    
    return nombre_masalto

nombre_masalto=obtener_nombre_persona_mas_alta(clientes_gimnasio)
print(f'La persona más alta es {nombre_masalto}.')

#Crea una función que devuelva el número de mujeres.

def obtener_numero_mujeres(clientes):

    numero_mujeres=0

    for cliente in clientes:
        genero=cliente[1]
        if genero=='F':
            numero_mujeres+=1
    return numero_mujeres

numero_mujeres=obtener_numero_mujeres(clientes_gimnasio)

print(f'El número de mujeres es de {numero_mujeres}.')

#Crea una función que devuelva una lista con los nombres de las mujeres.

def obtener_nombre_mujeres(clientes):

    nombre_mujeres=[]

    for cliente in clientes:
        nombre=cliente[0]
        genero=cliente[1]
        if genero=='F':
            nombre_mujeres.append(nombre)
    return nombre_mujeres

nombre_mujeres=obtener_nombre_mujeres(clientes_gimnasio)

print(f'El nombre de las mujeres es {nombre_mujeres}.')

def obtener_hombre_y_mujer_mas_alto(clientes):
    nombre_mas_alto_hombre_y_mujer=[]
    
    altura_max_masc=0
    altura_max_fem=0
    for cliente in clientes:
        nombre=cliente[0]
        altura=cliente[2]
        genero=cliente[1]
        if genero=='M':
            if altura>altura_max_masc:
                altura_max_masc=altura
                nombre_mas_alto_hombre_y_mujer.append(nombre)
        if genero=='F':
            if altura>altura_max_fem:
                altura_max_fem=altura
                nombre_mas_alto_hombre_y_mujer.append(nombre)
    return nombre_mas_alto_hombre_y_mujer

nombre_altos=(obtener_hombre_y_mujer_mas_alto(clientes_gimnasio))
print(nombre_altos)








def calcular_masa_corporal(masa_kg,estatura_metros):
    return round(masa_kg / estatura_metros ** 2, 2)

print(calcular_masa_corporal(68,165/100))

def mostrar_masas_corporales(clientes):
    print('Las masas corporales son: ')

    for cliente in clientes:
        masa_kg = cliente[3]
        estatura_metros = cliente[2] / 100
        masa_corporal = calcular_masa_corporal(masa_kg , estatura_metros)
        print(f'Cliente: {cliente[0]}, Masa Corporal: {masa_corporal}')

os.system('cls')

mostrar_masas_corporales(clientes_gimnasio)

os.system('cls')

def mostrar_masas_corporales_ordenadas(clientes):
    masas_corporales=[]
    for cliente in clientes:
        masa_kg = cliente[3]
        estatura_metros = cliente[2] / 100
        masa_corporal = calcular_masa_corporal(masa_kg , estatura_metros)
        masas_corporales.append([masa_corporal, cliente[0] ])
        masas_corporales.sort()
    print(masas_corporales)

mostrar_masas_corporales_ordenadas(clientes_gimnasio)
