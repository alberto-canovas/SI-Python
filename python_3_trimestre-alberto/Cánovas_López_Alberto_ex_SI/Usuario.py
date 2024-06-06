
class Usuario:
    
    def __init__(self, login:str,password:str,name:str) -> None:
        self.__login = login
        if not Usuario.correct_password(password):
            raise UsuarioError('la contraseña debe tener mínimo 8 caracteres')
        self.__password = password
        self.__name = name

    @property
    def login(self):
        return self.__login
   
    @property
    def name(self):
        return self.__name

    def correct_password(password:str)->bool:
        if len(password)<8:
            return False
        return True

    def comprobar_contraseña(self,contraseña:str) -> bool:
        if contraseña == self.__password:
            return True
        return False
        

class UsuarioError(Exception):
    ...
    