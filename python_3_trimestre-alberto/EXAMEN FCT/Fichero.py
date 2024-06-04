class Fichero:
    def __init__(self, nombre: str, tamaño:int) -> None:
        self.nombre = nombre
        self.tamaño = tamaño


    @property
    def tamaño(self):
        return self.tamaño
    

    @tamaño.setter
    def tamaño(self, valor:int):
        self.tamaño = valor

