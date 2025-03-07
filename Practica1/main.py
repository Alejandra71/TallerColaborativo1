from Estudiante import Estudiante
from Curso import Curso

list_student = []  # Lista para almacenar objetos de estudiantes
list_cursos = []  # Lista para almacenar objetos de cursos

def registrar_estudiante():
    print('\nRegistrar un estudiante')
    name = input('Nombre: ')
    address = input('Dirección: ')
    age = input('Edad: ')
    course_code = input('Código del curso: ')
    
    curso = next((c for c in list_cursos if c.codigo == course_code), None)
    if not curso:
        print('\nCurso no encontrado. Primero registre el curso.\n')
        return
    
    estudiante = Estudiante(name, age, address, curso)  # Creación de un objeto Estudiante
    list_student.append(estudiante)  # Agregar estudiante a la lista
    curso.agregar_estudiante(estudiante)
    print('\nEstudiante guardado con éxito\n')

def mostrar_estudiante():
    if len(list_student) == 0:
        print('\nNo hay estudiantes en la lista.\n')
    else:
        print('\n=== Listado de estudiantes registrados ===\n')
        for estudiante in list_student:
            print(estudiante)  # Imprimir directamente el objeto usando __str__
            

def actualizar_estudiante():
    nombre = input("\nIngrese el nombre del estudiante a actualizar: ")
    for estudiante in list_student:
        if estudiante.get_nombre().lower() == nombre.lower():
            print("\nDatos actuales: ")
            print(estudiante)
            estudiante.set_nombre(input("\nNuevo nombre: "))
            estudiante.set_direccion(input("Nueva dirección: "))
            estudiante.set_edad(input("Nueva edad: "))
            nuevo_curso_code = input("Nuevo código de curso: ")
            
            nuevo_curso = next((c for c in list_cursos if c.codigo == nuevo_curso_code), None)
            if nuevo_curso:
                estudiante.set_curso(nuevo_curso)
            else:
                print('\nCurso no encontrado, manteniendo el curso anterior.\n')
            
            print("\nEstudiante actualizado correctamente.\n")
            return
    print("\nEstudiante no encontrado.\n\n")

def eliminar_estudiante():
    nombre = input("\nIngrese el nombre del estudiante a eliminar: ")
    for estudiante in list_student:
        if estudiante.get_nombre().lower() == nombre.lower():
            list_student.remove(estudiante)
            curso = estudiante.get_curso()
            if estudiante in curso.estudiantes:
                curso.estudiantes.remove(estudiante)
            print(f"\nEstudiante '{nombre}' eliminado correctamente.\n")
            return
    print("\nEstudiante no encontrado.\n\n")



def registrar_curso():
    print('\nRegistrar curso')
    codigo = input('Código del curso: ')
    nombre = input('Nombre del curso: ')
    curso = Curso(codigo, nombre)
    list_cursos.append(curso)
    print('\nCurso guardado con éxito\n')

def mostrar_cursos():
    if len(list_cursos) == 0:
        print('\nNo hay cursos registrados.\n')
    else:
        print('\n=== Listado de cursos registrados ===\n')
        for curso in list_cursos:
            print(curso.mostrar_info())
            

while True:
    print('\n' + '=' * 50)
    print('::: MENU :::')
    print("""    \n    1. Registrar curso 
    2. Registrar estudiante  
    3. Consultar Listado de Estudiantes
    4. Consultar Listado de Cursos    
    5. Actualizar estudiante
    6. Eliminar estudiante
    7. Salir""")
    op = input('\nIngresa la opción que desea ejecutar: ')
    
    if op == '1':
        registrar_curso()
    elif op == '2':
        registrar_estudiante()
    elif op == '3':
        mostrar_estudiante()
    elif op == '4':
        mostrar_cursos()
    elif op == '5':
        actualizar_estudiante()
    elif op == '6':
        eliminar_estudiante()
    elif op == '7':
        print('\nSaliendo del sistema\n')
        break
    else:
        print('\nOpción inválida\n')
