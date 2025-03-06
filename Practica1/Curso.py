class Curso:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_info(self):
        return f'Código: {self.codigo}, \n Nombre: {self.nombre}, \n Estudiantes inscritos: {len(self.estudiantes)}'
