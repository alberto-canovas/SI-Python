from PuertoRed import PuertoRed

class Conmutador:
    #__cantidad_puertos: ...
    __encendido: bool = False
    __puertos: list[PuertoRed] = []
    
    def __init__(self, cantidad_puertos: int) -> None:
        self.__cantidad_puertos = cantidad_puertos


    #get
    @property
    def encendido(self) -> bool:
        return self.__encendido


    @property
    def puertos(self)-> list[PuertoRed]:
        return self.__puertos


    @property
    def cantidad_puertos(self)-> int:
        return self.__cantidad_puertos    


    def encender(self):
        self.__encendido= True

    def apagar(self):
        self.__encendido= False
    
    def añadir_puerto(self, puerto: PuertoRed):

        if self.__encendido:
            raise ConmutadorError('ERROR, debe apagar el switch/conmutador primero.')
        elif len(self.__puertos) == self.__cantidad_puertos:
            raise ConmutadorError('ERROR, el switch/conmutador está completo.')
        else: 
            self.__puertos.append(puerto)


class ConmutadorError(Exception):
    ...
