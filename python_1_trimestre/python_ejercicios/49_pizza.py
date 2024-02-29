import os
os.system('cls')


ingredientes = [
    {'nombre': 'Base de pizza', 'cantidad': 1, 'precio': 0.90},
    {'nombre': 'Salsa de tomate', 'cantidad': 1 , 'precio': 0.25},
    {'nombre': 'Jamón de york', 'cantidad': 2, 'precio': 0.40},
    {'nombre': 'Queso rallado', 'cantidad': 2, 'precio': 0.20},
    {'nombre': 'Aceitunas', 'cantidad': 1, 'precio': 0.25},
    {'nombre': 'Salami', 'cantidad': 1, 'precio': 0.45},
    {'nombre': 'Orégano', 'cantidad': 1, 'precio': 0.10},
    {'nombre': 'Alcaparras', 'cantidad': 1, 'precio': 0.15},
]

# Desarrolla una función que calcule la base imponible total (los precios de arriba son antes de impuestos).

def calcular_precio_pizza(ingredientes):
    precio_total = 0
    for ingrediente in ingredientes:
        precio = ingrediente['cantidad']*ingrediente['precio']
        precio_total = precio_total + precio
    return round(precio_total,3)


# Desarrolla una función que calcule el precio total teniendo en cuenta que el IVA que se aplica a los restaurantes es del 10%.

def calcular_precio_mas_iva(iva):
    iva=0.1
    precio_mas_iva=calcular_precio_pizza(ingredientes)+(calcular_precio_pizza(ingredientes)*iva)
    return precio_mas_iva


# Desarrolla una función que imprima por pantalla algo parecido a un ticket o factura con todos los productos, ...

def imprimir_ticket(ingredientes):
    print('PRODUCTO                 CANTIDAD  PRECIO')
    for ingrediente in ingredientes:
        print(f'{ingrediente['nombre']:20}{ingrediente['cantidad']:10}{ingrediente['precio']:10}')
    
    print('******************************************')
    print(f'PRECIO TOTAL SIN IVA {calcular_precio_pizza(ingredientes)}')
    print(f'TOTAL MÁS IVA {calcular_precio_mas_iva(ingredientes)}')


imprimir_ticket(ingredientes)


