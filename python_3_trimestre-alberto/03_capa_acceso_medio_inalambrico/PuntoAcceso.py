class PuntoAcceso:

    def __init__(self,ssid: str, contraseña: str) -> None:
        self.ssid = ssid
        self.contraseña = contraseña
        self.equipos_conectados: list[str] =[]
    
    def conectar(self, direccion_fisica:str, contraseña: str):
        if contraseña == self.contraseña:
            self.equipos_conectados.append(direccion_fisica)
        else:
            raise Exception('ERROR: La contraseña no es correcta')
        
        
            
class PuntoAccesoError(Exception):
    ...

