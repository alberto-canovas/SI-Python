import socket

EQUIPO = '192.168.0.38'
PUERTO = 8080

print(f'Servidor escuchando en el puerto {PUERTO}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((EQUIPO,PUERTO))
    s.listen()
    conexion, direccion_remota = s.accept()
    print(f'Cliente conectado desde el equipo {direccion_remota}')
    while True:
        mensaje = conexion.recv(1024)
        print(f'Mensaje recibido: {mensaje!r}')

