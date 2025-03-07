class Curso:
    def _init_(self, nombre, codigo):
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
    
    def _str_(self):
        return f"Curso: {self._nombre} (Código: {self._codigo})"