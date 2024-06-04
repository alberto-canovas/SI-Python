from Usuario import Usuario,UsuarioError
from Fichero import Fichero


class ServidorFtp:

    __capacidad_servidor:int
    __usuarios_registrados: dict[str,Usuario]
    __ficheros_almacenados:dict[str,list[Fichero]]

    def __init__(self,capacidad_servidor:int) -> None:
        self.__capacidad_servidor=capacidad_servidor
        #self.__usuarios_registrados
        #self.__ficheros_almacenados
    
    @property
    def capacidad(self):
        return self.__capacidad_servidor
    
    @property
    def usuarios_registrados(self):
        return self.__usuarios_registrados
    
    @property
    def ficheros_almacenados(self):
        return self.__ficheros_almacenados

    def obtener_nombre_completo_usuario(self,login):
        login=self.usuarios_registrados.keys()
        if login == Usuario.login:
            return f'{Usuario.name}'
            


    def registrar_usuario(self,login,usuario:Usuario):
        if login in self.__usuarios_registrados.keys():
            raise FtpUsuarioError('ERROR - El usuario ya está registrado.')
        else:
            self.__usuarios_registrados.update(login,usuario)

    

    def calcular_almacenamiento_ocupado(self)->int:
        tamaño_ficheros = Fichero.tamaño + tamaño_ficheros
        capacidad=self.capacidad - tamaño_ficheros
        if capacidad<0:
            raise FtpFicheroError('ERROR - No queda capacidad.')
        
        return f'Capacidad ocupada: {tamaño_ficheros}, Capacidad libre: {capacidad}'
    
    def almacenar_fichero(self,usuario,fichero):
        
        nombre=input('Introduce el nombre: ')
        if nombre in self.ficheros_almacenados.keys():
            raise FtpFicheroError('ERROR - Ya existe un fichero con ese nombre')
        
        tamaño=input('Introduce el tamaño: ')
        if tamaño<=0:
            raise FtpFicheroError('ERROR - El tamaño del fichero debe de ser mayor que 0 ')

        fichero=Fichero(nombre,tamaño)

        self.ficheros_almacenados.update(nombre,fichero)

    def son_usuario_y_contraseña_validos(self, login, contraseña)-> bool:
        if login not in ServidorFtp.usuarios_registrados and contraseña not in ServidorFtp.usuarios_registrados:
            raise FtpUsuarioError('El usuario o la contraseña son incorrectos')
        
        return True

    def obtener_ficheros_almacenados_por_usuario(self,usuario)->list[Fichero]:
        ...
    
    def obtener_ficheros_almacenados(self)->list[Fichero]:
        if len(list[Fichero])==0:
            raise FtpFicheroError('No hay ficheros subidos')
        else:
            print('Los ficheros subidos son: ')
            for fichero in list[Fichero]:
                print(f'    * {fichero}')





class FtpFicheroError(Exception):
    ...

class FtpUsuarioError(Exception):
    ...