from Carta import Carta, Palo, ValorCarta

class Baraja(list):
    def __init__(self):
        for palo in Palo:
            for valor in range(1,13):
                carta = Carta(valor,palo)
                #siempre que estoy en la misma clase para referirnos al objeto de la clase utilizamos self.
                self.append(carta) 
