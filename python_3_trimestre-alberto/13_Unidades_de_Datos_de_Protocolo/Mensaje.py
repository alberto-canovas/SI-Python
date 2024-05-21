type Telefono = int

class Mensaje:

    def __init__(self, mensaje: str, telefono_emisor: Telefono, telefono_receptor: Telefono, hora_envio:str) -> None:
        """Un reels representa un tipo de información que gestiona WhatsApp."""
        self.mensaje = mensaje
        self.emisor = telefono_emisor
        self.receptor = telefono_receptor
        self.hora_envio = hora_envio

