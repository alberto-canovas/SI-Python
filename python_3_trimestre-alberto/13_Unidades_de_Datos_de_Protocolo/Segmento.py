class Segmento: 
    def __init__(self, pueto_origen: int, pueto_destino: int, numero_secuencia:int, suma_verificacion: bytes, datos: bytes) -> None:
        """ Un segmento representa la información que gestiona la capa de Transporte"""
        
        self.puerto_origen = pueto_origen
        self.pueto_destino = pueto_destino
        self.numero_secuencia = numero_secuencia
        self.suma_verificacion = suma_verificacion
        self.datos = datos
        
        