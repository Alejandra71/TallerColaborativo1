''' Integrantes: 
    Maria de los Angeles Flores
    Luis Alejandro Gordillo
    Leslie Alejandra Guerrero 
    Diana Marcela Patiño
'''

from Persona import Persona

class Docente(Persona):
    def _init_(self, nombre, edad, direccion, curso):
        super()._init_(nombre, edad, direccion)
        if not isinstance(curso, str) or not curso.strip():
            raise ValueError("El curso debe ser un curso válido")
        self.__curso = curso
    
    def get_curso(self):
        return self.__curso
    
    def set_curso(self, curso):
        if not isinstance(curso, str) or not curso.strip():
            raise ValueError("El curso debe ser un curso válido")
        self.__curso = curso
    
    def _str_(self):
        return f"Docente: {super()._str()} - Curso: {self._curso}"''' Integrantes: 
    Maria de los Angeles Flores
    Luis Alejandro Gordillo
    Leslie Alejandra Guerrero 
    Diana Marcela Patiño
'''

from Persona import Persona

class Docente(Persona):
    def _init_(self, nombre, edad, direccion, curso):
        super()._init_(nombre, edad, direccion)
        if not isinstance(curso, str) or not curso.strip():
            raise ValueError("El curso debe ser un curso válido")
        self.__curso = curso
    
    def get_curso(self):
        return self.__curso
    
    def set_curso(self, curso):
        if not isinstance(curso, str) or not curso.strip():
            raise ValueError("El curso debe ser un curso válido")
        self.__curso = curso
    
    def _str_(self):
        return f"Docente: {super()._str()} - Curso: {self._curso}"