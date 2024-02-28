




def numero_a_mes(mes):
    #if not mes.isnumeric:
    #    raise Exception('Debe introducir un número.')
    if mes < 1 or mes > 12:
        raise Exception('Debe introducir un número entre 1 y 12.')

    match mes:
        case 1:
            return('Enero')
        case 2:
            return('Febrero')
        case 3:
            return('Marzo')
        case 4:
            return('Abril')
        case 5:
            return('Mayo')
        case 6:
            return('Junio')
        case 7:
            return('Julio')
        case 8:
            return('Agosto')
        case 9:
            return('Septiembre')
        case 10:
            return('Octubre')
        case 11:
            return('Noviembre')
        case 12:
            return('Diciembre')


for i in range(0,14):
    try:
        print(numero_a_mes(i))  

    except Exception as error:
        print(error)

(""")
try:
    print(numero_a_mes)
except Exception as error:
    print(error)
(""")
