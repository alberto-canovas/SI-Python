import os
os.system('cls')

datos_poblacionales_ciudades_grandes = [
    ['Cáceres',   17001,  185294, 3162876],
    ['La Coruña', 42001,  719458, 2371974],
    ['Barcelona',  3001, 2492654, 3258453],
    ['Murcia',    30001,  727432, 2836493],
    ['Madrid',     7001, 4036721, 3347365],
    ['Córdoba',   24001,  269351, 2637296],
]

datos_poblacionales_ciudades_pequenias = [
    ['Lorca',        30801,  94528, 76628],
    ['Villagarcía',  42032,  72863, 47197],
    ['Badalona',      3043, 324624, 25841],
    ['Huercalovera', 23043,  32236, 43647],
    ['Carabanchel',    7321, 436528, 34364],
    ['Torremolinos', 21032,  29734, 23732],
]

datos_fiscales_ciudades_grandes = [
    ['Murcia',    180665738952],
    ['La Coruña', 192377313536],
    ['Córdoba',    63818409834],
    ['Cáceres',    42153829118],
    ['Madrid',   1326131472757],
    ['Barcelona', 765581286290],
]

datos_fiscales_ciudades_pequenias = [
     ['Torremolinos', 7098784362],
     ['Carabanchel',   133933774848],
     ['Villagarcía',  19634538336],
     ['Badalona',     96716851440],
     ['Huercalovera', 7036119484],
     ['Lorca',        21380153984],
 ]



#Crear una función para juntar todo en una única lista de dos dimensiones en lugar de tener cuatro listas. 
#Por ejemplo, en la lista Lorca quedaría como:


def agrupar_datos(datos_poblacionales,datos_fiscales):
    datos_totales=[]
    for dato_poblacional in datos_poblacionales:
        for dato_fiscal in datos_fiscales:
            if dato_poblacional[0]==dato_fiscal[0]:
                nuevo_dato=[dato_poblacional[0],dato_poblacional[1],dato_poblacional[2],dato_poblacional[3],dato_fiscal[1]]
                datos_totales.append(nuevo_dato)
                break
    return datos_totales



def juntar_todos_los_datos(datos_poblacionales_ciudades_pequenias,datos_fiscales_ciudades_pequenias,datos_poblacionales_ciudades_grandes,datos_fiscales_ciudades_grandes):
    datos=[]
    datos_grandes=agrupar_datos(datos_poblacionales_ciudades_grandes,datos_fiscales_ciudades_grandes)
    datos_pequenias=agrupar_datos(datos_poblacionales_ciudades_pequenias,datos_fiscales_ciudades_pequenias)
    for dato in datos_grandes:
        datos.append(dato)
    for dato in datos_pequenias:
        datos.append(dato)
    return datos

# print(juntar_todos_los_datos(datos_poblacionales_ciudades_pequenias,datos_fiscales_ciudades_pequenias,datos_poblacionales_ciudades_grandes,datos_fiscales_ciudades_grandes))


def convertir_en_diccionario(datos):
    datos_diccionario_suma=[]

    for dato in datos:
        datos_diccionario={
            'nombre':dato[0],
            'codigo_postal':dato[1],
            'población':dato[2],
            'superficie':dato[3],
            'riqueza':dato[4],}
        datos_diccionario_suma.append(datos_diccionario)
    return datos_diccionario_suma

# datos_unidos = juntar_todos_los_datos(datos_poblacionales_ciudades_pequenias,datos_fiscales_ciudades_pequenias,datos_poblacionales_ciudades_grandes,datos_fiscales_ciudades_grandes)
# print(convertir_en_diccionario(datos_unidos))

def sumar_poblacion_ciudades(poblacion_total):

    poblacion_total_suma=0
    for poblacion_ciudad in poblacion_total:
       poblacion_total_suma += poblacion_ciudad[2]
    return poblacion_total_suma

# datos_poblacion_total=juntar_todos_los_datos(datos_poblacionales_ciudades_pequenias,datos_fiscales_ciudades_pequenias,datos_poblacionales_ciudades_grandes,datos_fiscales_ciudades_grandes)
# print(sumar_poblacion_ciudades(datos_poblacion_total))

def sumar_superficie_pais (datos):
    superficie_total=0
    for dato in datos:
        superficie_total+=dato[3]
    return superficie_total

datos=juntar_todos_los_datos(datos_poblacionales_ciudades_pequenias,datos_fiscales_ciudades_pequenias,datos_poblacionales_ciudades_grandes,datos_fiscales_ciudades_grandes)
print(f'Superficie: {sumar_superficie_pais(datos)}.')

def obtener_pib(datos):
    pib=0
    for dato in datos:
        pib+=dato[4]
    return pib

print(f'PIB: {obtener_pib(datos)}.')


def devolver_informacion_ciudad(datos):
    ciudad=''
    








# def agrupar_datos(datos_fiscales_ciudades_grandes,datos_poblacionales_ciudades_grandes):

#     datostotales_ciudades_grandes=[]

#     for i in range(0,len(datos_poblacionales_ciudades_grandes)):
#         for i in range(0,len(datos_fiscales_ciudades_grandes)):
#             if datos_poblacionales_ciudades_grandes[i][0]==datos_fiscales_ciudades_grandes[i][0]:
#                 datostotales_ciudades_grandes.append(datos_poblacionales_ciudades_grandes)

#     return datostotales_ciudades_grandes

# print(agrupar_datos(datos_fiscales_ciudades_grandes,datos_poblacionales_ciudades_grandes))
