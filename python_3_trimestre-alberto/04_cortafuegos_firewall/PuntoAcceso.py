from enum import Enum, auto


class TipoFiltrado(Enum):
    LISTA_BLANCA = auto()
    LISTA_NEGRA = auto()


class PuntoAcceso:

    def __init__(self, ssid: str, password: str) -> None:
        self.__ssid = ssid
        self.__password = password
        self.__equipos_conectados: list[str] = []
        self.__esta_cortafuegos_activado: bool = False
        self.__tipo_filtrado: TipoFiltrado = TipoFiltrado.LISTA_BLANCA
        self.__equipos_filtrados: list[str] = []

    @property 
    def tipo_filtrado(self) -> TipoFiltrado:
        return self.__tipo_filtrado
    
    @tipo_filtrado.setter
    def tipo_filtrado(self, valor: TipoFiltrado) -> None:
        self.__tipo_filtrado = valor

    @property
    def equipos_filtrados(self) -> str:
        return self.__equipos_filtrados

    def agregar_equipo_filtrado(self, equipo: str) -> None:
        self.__equipos_filtrados.append(equipo)

    def desagregar_equipo_filtrado(self, equipo: str) -> None:
        self.__equipos_filtrados.remove(equipo)


    @property
    def esta_cortafuegos_activado(self) -> bool:
        return self.__esta_cortafuegos_activado
    
    def activar_cortafuegos(self):
        self.__esta_cortafuegos_activado = True

    def desactivar_cortafuegos(self):
        self.__esta_cortafuegos_activado = False


    @property
    def ssid(self) -> str:
        return self.__ssid
    
    @ssid.setter
    def ssid (self,new_ssid: str) -> None:
        self.__ssid = new_ssid


    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password (self,new_password: str) -> None:
        self.__password = new_password

    
    @property
    def equipos_conectados(self) -> str:
        return self.__equipos_conectados
    

    @equipos_conectados.setter
    def equipos_conectados (self,new_equipos_conectados: str) -> None:
        self.__equipos_conectados = new_equipos_conectados

    def conectar_equipo(self, direccion_equipo: str, password: str)-> None:
        if self.esta_cortafuegos_activado:
            if self.tipo_filtrado == TipoFiltrado.LISTA_BLANCA:
                if self.__equipos_filtrados.count(direccion_equipo) != 0:
                    self.__equipos_conectados.append(direccion_equipo)
                else: 
                    raise PuntoAccesoError ('El equipo no está en la whitelist')
            
            else: #LISTA NEGRA
                if self.__equipos_filtrados.count(direccion_equipo) == 0:
                    self.__equipos_conectados.append(direccion_equipo)
                else:
                    raise PuntoAccesoError('El equipo está en la blacklist')

        else: #cortafuegos desactivado

            if password == self.password:
                self.__equipos_conectados.append(direccion_equipo)
            else:
                raise PuntoAccesoError('Contraseña incorrecta') 
        

    def desconectar_equipo(self, direccion_equipo: str) -> None:
        self.equipos_conectados.remove(direccion_equipo)

class PuntoAccesoError (Exception):
    ...