from enum import Enum

type Aplicacion = str
type NumeroPuerto = int


class TipoServicio(Enum):
    UDP = 'udp'
    TCP = 'tcp'

class Puerto:

    def __init__(self, numero_puerto: NumeroPuerto, tipo_servicio: TipoServicio) -> None:
        self.numero_puerto = numero_puerto
        self.tipo_servicio = tipo_servicio
        