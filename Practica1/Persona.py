class Persona:
    def __init__(self, nombre, edad, direccion):
        
        self.__nombre=nombre
        self.__edad=edad
        self.__direccion=direccion

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre= nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad= edad

    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self, direccion):
        self.__direccion= direccion

    def __str__(self):
        return f" Nombre: {self.get_nombre()} \n Edad: {self.get_edad()} \n Dirección: {self.get_direccion()}"

    
    