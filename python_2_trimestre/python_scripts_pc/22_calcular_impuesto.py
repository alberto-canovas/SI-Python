import subprocess,sys


impuesto_valor_añadido = [
    {
        "año" : 2024,
        "exento" : 0.0,
        "superreducido" : 4.0,
        "reducido" : 10.0,
        "normal" : 21.0,
    },
    {
        "año" : 2013,
        "exento" : 0.0,
        "superreducido" : 4.0,
        "reducido" : 10.0,
        "normal" : 21.0,
    },
    {
        "año" : 2012,
        "exento" : 0.0,
        "superreducido" : 4.0,
        "reducido" : 8.0,
        "normal" : 18.0
    },
    {
        "año" : 2010,
        "exento" : 0.0,
        "superreducido" : 4.0,
        "reducido" : 7.0,
        "normal" : 16.0,
    },

]

tipos_impuestos = ["exento","superreducido","reducido","normal"]

def main():
    argumentos=sys.argv[1:]
    try:
        limpiar_pantalla()
        obtener_fecha_actual()
        #son_argumentos_correctos(argumentos)
        obtener_base_imponible(argumentos)
        obtener_tipo_impuesto(argumentos)
        #calcular_importe_tras_impuestos(argumentos)
    except Exception as error:
         print(error)

def son_argumentos_correctos(argumentos):
    base_imponible = argumentos[0]
    tipo_impuesto = argumentos[1]
    

    if len(argumentos)!=2 or 3:
        raise Exception(f'Debe introducir 2 o 3 argumentos.')
        
    if not base_imponible.isnumeric():
        raise Exception ('El primer argumento debe de ser un número positivo.')

    if not tipos_impuestos.__contains__(tipo_impuesto):
         raise Exception('El segundo argumento debe de ser (exento), (reducido), (superreducido) o (normal).')


def obtener_base_imponible(argumentos):
    base_imponible = argumentos[0]
    if not base_imponible.isnumeric():
         raise Exception ('El primer argumento debe de ser un número positivo.')
    print(f'base imponible ok {base_imponible}')
    return base_imponible


def obtener_tipo_impuesto(argumentos):
    tipo_impuesto = argumentos[1]
    # if not tipo_impuesto ==  'exento' or 'reducido' or 'superreducido' or 'normal':
    #      raise Exception('El segundo argumento debe de ser (exento), (reducido), (superreducido) o (normal).')
    print(f'tipo de impuesto ok {tipo_impuesto}')
    return tipo_impuesto  



def obtener_fecha_actual():
    subprocess.run(['date','+"%d/%m/%Y"'])
     


def calcular_importe_tras_impuestos(argumentos):

    base_imponible = argumentos[0]  
    tipo_impuesto = argumentos[1]

    importe_final =obtener_base_imponible(base_imponible)* 5
    return print(importe_final)







def limpiar_pantalla():
    subprocess.run('clear')

if __name__ == '__main__':
    main()