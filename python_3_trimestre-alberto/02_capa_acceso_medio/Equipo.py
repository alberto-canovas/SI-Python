from PuertoRed import PuertoRed

class Equipo:

    def __init__(self,nombre: str) -> None:
        self.__nombre = nombre


    @property
    def nombre(self)-> str:
        return self.nombre
    

    def añadir_puerto_red(self,puerto: PuertoRed):
        self.__puerto = puerto
