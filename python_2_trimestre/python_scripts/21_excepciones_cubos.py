cubo_uno = {
    "capacidad":5,
    "contenido":0
}

cubo_dos = {
    "capacidad":3,
    "contenido":0
}

cubo_tres = {
    "capacidad":2,
    "contenido":0
}

def llenar_cubo(cubo):
    if cubo["contenido"]==cubo["capacidad"]:
        raise Exception('El cubo ya está lleno')
    cubo["contenido"]=cubo["capacidad"]
    print(cubo)

def vaciar_cubo_en_otro(cubo_a_vaciar,cubo_a_llenar):
    if cubo_a_llenar["contenido"]==cubo_a_llenar["capacidad"] or cubo_a_llenar["contenido"] > cubo_a_llenar["capacidad"] :
        raise Exception('El cubo a llenar está al máximo de su capacidad.')
    cubo_a_vaciar["contenido"]+=cubo_a_llenar["contenido"]
    print(f'El cubo a llenar tiene {cubo_a_llenar}')
    print(f'El cubo a vaciar tiene {cubo_a_vaciar}')


try:
    print(cubo_tres)
    llenar_cubo(cubo_tres)
    #llenar_cubo(cubo_tres)
    vaciar_cubo_en_otro(cubo_tres,cubo_uno)
except Exception as error:
    print(error)

