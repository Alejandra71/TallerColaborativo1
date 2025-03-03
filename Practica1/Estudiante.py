from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion)
        self.__curso=curso

    def getcurso(self):
        return self.__curso
    
    def setcurso(self, curso):
        self.__curso = curso

    
    def __str__(self):
        print(f"Los datos del estudiante son los siguiente: \n", super().__str__(), "\n Matriculado en el curso: ", self.getcurso)