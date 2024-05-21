from enum import Enum, auto



class TipoWifi(Enum):
    WIFI1 = auto()
    WIFI2 = auto()
    WIFI3 = auto()
    WIFI4 = auto()
    WIFI5 = auto()
    WIFI6 = auto()
    
class PuntoAcceso:
    """
    Un punto de acceso permite añadir dispositivos analámbricos a la red.
    """


    def __init__(self, ssid: str, password: str, tipos_wifi: list[TipoWifi])-> None:
        self.__ssid = ssid
        self.__password = password
        self.__tipos_wifi = tipos_wifi



    @property
    def ssid(self) -> str:
        return self.__ssid
    
    @ssid.setter
    def ssid(self, new_ssid: str) -> None:
        self.__ssid  = new_ssid
     
     

    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, new_password: str) -> None:
        self.__password = new_password


    @property
    def tipos_wifi(self)-> str:
        return self.__tipos_wifi