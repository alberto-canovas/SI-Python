
class Usuario:
    
    def __init__(self, login:str,password:str,name:str) -> None:
        self.__login = login
        self.__password = password
        self.__name = name

    @property
    def login(self):
        return self.__login
    
    # @login.setter
    # def login(self,new_login:str):
    #     self.__login = new_login

    # @property
    # def password(self):
    #     return self.__pasword
    
    # @password.setter
    # def password(self,new_password:str):
    #     self.__pasword = new_password

    @property
    def name(self):
        return self.__name
    
    # @name.setter
    # def nombre(self,new_name:str):
    #     self.__name = new_name


    def correct_password(self,password:str)->bool:
        if len(password)<8:
            raise UsuarioError('ERROR La contraseña debe de tener 8 caracteres o más')
            return False
        return True



class UsuarioError(Exception):
    ...
    