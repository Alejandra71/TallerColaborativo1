class Curso:
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo

    # Métodos Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_codigo(self):
        return self.__codigo

    # Métodos Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def __str__(self):
        return f"Curso: {self.__nombre} (Código: {self.__codigo})"