''' Integrantes: 
    Maria de los Angeles Flores
    Luis Alejandro Gordillo
    Leslie Alejandra Guerrero 
    Diana Marcela Patiño
    
  '''   
from Persona import Persona
from Curso import Curso 

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion)
        self.__curso = curso 
    

    def get_curso(self):
        return self.__curso
    
 
    def set_curso(self, curso):
        if isinstance(curso, Curso):
            self.__curso = curso
        else:
            raise ValueError("El curso debe ser una instancia de la clase Curso")
    
    def __str__(self):
        return f"{super().__str__()}\nMatriculado en: {self.__curso}"