import socket
from config import IP_SERVIDOR,PUERTO
from threading import Thread

class Cliente:
    

    def conectar_a_servidor(self, ip_servidor, puerto_servidor):
        print(f'Intentando conectar al servidor y puerto ({ip_servidor}, {puerto_servidor})')

        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket_cliente:
            socket_cliente.connect((ip_servidor,puerto_servidor))
            hilo_recibir = Thread(target=self.__recibir, args=(socket_cliente,))
            hilo_enviar = Thread(target=self.__enviar, args=(socket_cliente,))
            hilo_recibir.start()
            hilo_enviar.start()
            hilo_recibir.join()
            hilo_enviar.join()
    def __enviar(self,socket_cliente):
        while True:
            mensaje = input('\033[0;32;40m>>> Mensaje a enviar: ')
            socket_cliente.send(mensaje.encode())

    def __recibir(self, socket_cliente):
        while True:
            mensaje = socket_cliente.recv(1024)
            print(f'\033[0;34;40m<<<{mensaje.decode()}')


def main():
    cliente = Cliente()
    cliente.conectar_a_servidor(IP_SERVIDOR,PUERTO)

if __name__=='__main__':
    main()