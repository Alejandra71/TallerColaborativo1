from Curso import Curso

class Estudiante:
    def __init__(self, nombre, edad, direccion, curso):
        if not isinstance(curso, Curso):
            raise TypeError("El curso debe ser una instancia de la clase Curso.")
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.curso = curso

    # Métodos GET
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_direccion(self):
        return self.direccion

    def get_curso(self):
        return self.curso

    # Métodos SET
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        self.edad = nueva_edad

    def set_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def set_curso(self, nuevo_curso):
        if not isinstance(nuevo_curso, Curso):
            print("El curso asignado no es válido.")
            return
        self.curso = nuevo_curso

    # Método para mostrar información del estudiante
    def __str__(self):
        return f"Nombre: {self.nombre}, \n Edad: {self.edad}, \n Dirección: {self.direccion}, \n Curso: {self.curso.nombre}"
