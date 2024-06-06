from Usuario import Usuario,UsuarioError
from Fichero import Fichero


class ServidorFtp:

    __capacidad_servidor:int
    __usuarios_registrados: dict[str,Usuario]
    __ficheros_almacenados:dict[str,list[Fichero]]

    def __init__(self,capacidad_servidor:int) -> None:
        self.__capacidad_servidor=capacidad_servidor
        self.__usuarios_registrados : dict[str,Usuario] = {}
        self.__ficheros_almacenados : dict[str,list[Fichero]] = {}
    
    @property
    def capacidad(self):
        return self.__capacidad_servidor
    
    @property
    def usuarios_registrados(self):
        return self.__usuarios_registrados
    
    @property
    def ficheros_almacenados(self):
        return self.__ficheros_almacenados

    def obtener_nombre_completo_usuario(self,login:str):
        if login in self.__usuarios_registrados.keys():
            return self.__usuarios_registrados[login].name
        
        else:
            raise FtpUsuarioError(f'ERROR - El usuario {login} no está registrado')
            

    def registrar_usuario(self,login,usuario:Usuario):
        if login in self.__usuarios_registrados.keys():
            raise FtpUsuarioError(f'ERROR - El usuario {login} ya está registrado.')
        else:
            self.__usuarios_registrados[login] = usuario

    

    def calcular_almacenamiento_ocupado(self)->int:
        tamaño_ficheros = 0
        for lista_ficheros in self.ficheros_almacenados.values():
            for fichero in lista_ficheros:
                tamaño_ficheros = fichero.tamaño + tamaño_ficheros

        capacidad_libre = self.capacidad - tamaño_ficheros
        if capacidad_libre<0:
            raise FtpFicheroError('ERROR - No queda capacidad en el servidor')
        
        return f'Capacidad ocupada {tamaño_ficheros}, Capacidad libre: {capacidad_libre}'
    
        # tamaño_ficheros = Fichero.tamaño + tamaño_ficheros
        # capacidad=self.capacidad - tamaño_ficheros
        # if capacidad<0:
        #     raise FtpFicheroError('ERROR - No queda capacidad.')
        
        # return f'Capacidad ocupada: {tamaño_ficheros}, Capacidad libre: {capacidad}'
    
    def almacenar_fichero(self,login:str,nombre:str,tamaño:int):
        
        if nombre in self.__ficheros_almacenados[login].nombre:
            raise FtpFicheroError('ERROR - Ya existe un fichero con ese nombre')
        
        if tamaño<=0:
            raise FtpFicheroError('ERROR - El tamaño del fichero debe de ser mayor que 0 ')

        fichero=Fichero(nombre,tamaño)

        self.ficheros_almacenados[login] = fichero

    def son_usuario_y_contraseña_validos(self, login, contraseña)-> bool:
        if login not in self.usuarios_registrados.keys() and contraseña not in self.usuarios_registrados[login].comprobar_contraseña():
            raise FtpUsuarioError('El usuario o la contraseña son incorrectos')
        
        return True

    def obtener_ficheros_almacenados_por_usuario(self,usuario)->list[Fichero]:
        ...
    
    def obtener_ficheros_almacenados(self)->list[Fichero]:
        if len(list[Fichero])==0:
            raise FtpFicheroError('No hay ficheros subidos')
        else:
            print('Los ficheros subidos son: ')
            for fichero in list[Fichero.nombre]:
                print(f'    * {fichero}')





class FtpFicheroError(Exception):
    ...

class FtpUsuarioError(Exception):
    ...