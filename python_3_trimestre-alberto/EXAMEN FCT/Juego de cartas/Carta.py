from enum import Enum, auto


class Palo(Enum):
    OROS = auto()
    COPAS = auto()
    ESPADAS = auto()
    BASTOS = auto()



type ValorCarta = int




class Carta:
    def __init__(self, valor: ValorCarta, palo: Palo) -> None:
        self.valor = valor
        self.palo = palo

    def __eq__(self, value: object) -> bool:
        ...