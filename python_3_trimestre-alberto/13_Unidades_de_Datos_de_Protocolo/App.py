from Mensaje import Mensaje
import pickle

# mensaje = Mensaje('hola que tal 🏳‍🌈', 666111000, 666999000,'2024-05-16 11:50')

alumno = {
    'nombre':'Jimena',
    'apellido':'Sánchez',
    'edad': 39,
    'aficiones':['cantar','bailar','programar'],
    'avatar':'🏳‍🌈'
}


def serializar(informacion: object) ->bytes:
    return pickle.dumps(informacion)

def deserializar(datos: bytes) -> object:
    return pickle.loads(datos)


print(alumno)
alumno_serializado =serializar(alumno)
print(alumno_serializado)
alumno_deserializado = deserializar(alumno_serializado)
print(alumno_deserializado)


# alumno_serializado = pickle.dumps(alumno)
# print(alumno)
# print(alumno_serializado)
# #guardariamos alumno en un fichero o lo enviariamos por la red
# alumno_desearializado = pickle.loads(alumno_serializado)
# print(alumno_desearializado)