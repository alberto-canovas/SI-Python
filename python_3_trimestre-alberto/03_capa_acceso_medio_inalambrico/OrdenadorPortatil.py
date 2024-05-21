from Equipo import Equipo

class OrdenadorPortatil(Equipo):

    #ESTO ES LO MISMO QUE TO.STRING 
    def __repr__(self) -> str: 
        return f'[OrdenadorPortatil] {self.nombre} {self.direccion_fisica}'

