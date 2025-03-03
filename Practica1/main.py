# main.py
from Estudiante import Estudiante

list_student = []  # Lista para almacenar objetos de clientes

def registrar_estudiante():
        print('Se va a registrar un estudiante')
        name = input('Ingresar el nombre: ')
        address = input('Ingrese el dirección: ')
        age = input('Ingrese la edad: ')
        course=input('Ingresar el curso')

        estudiante = Estudiante(name, age, address,course)  # Creación de un objeto Cliente
        list_student.append(estudiante)  # Agregar estudiante a la lista
        print('Estudiante guardado con éxito')

def mostrar_estudiante():
        
        if len(list_student) == 0:
            print("No hay cliente en la lista.")
        else:
            print('Se va a mostrar un listado de clientes')
            for estudiante in list_student:
                estudiante.mostrar_informacion()  # Llamamos al método para mostrar información
                
"""def eliminar_cliente(nombre):
        for cliente in list_clientes:
            if cliente.get_name().lower() == nombre.lower():
                list_clientes.remove(cliente)
                print(f"Cliente '{nombre}' eliminado con éxito.")
                return
        print(f"Cliente '{nombre}' no encontrado.")
        
def actualizar_contacto(nombre, new_phone):
        for cliente in list_clientes:
            if cliente.get_name().lower() == nombre.lower():
                try:
                    cliente.set_phone(new_phone)
                    print(f"El telefono de '{nombre}' fue actualizado a {new_phone}.")
                except ValueError as e:
                    print(f"Error: {e}")
                return
        print(f"Cliente '{nombre}' no encontrado.")
"""

while True:
    print('::: MENU :::')
    print("""    1. Registrar estudiante 
    2. Consultar Listado
    3. Actualizar cliente
    4. Eliminar un cliente 
    5. salir""")
    op = input('ingresa la opcion que desee ejecutar')
    
    if op == '1':
        registrar_estudiante()
        
    elif op == '2':
        mostrar_estudiante()
    
    """elif op == '3':
       nombre = input("Ingresa el nombre del estudiante a actualizar: ")
       try:
                new_phone = int(input(f"Ingresa el nuevo telefono de '{nombre}': "))
                actualizar_contacto(nombre, new_phone)
       except ValueError:
                print("Error: el telefono debe ser un número.")
    elif op == '4':
         nombre = input("Ingresa el nombre del producto a eliminar: ")
         eliminar_cliente(nombre)
    
    elif op == '5':
        print('saliendo del sistemas')
        exit()
    else:
        print('opcion invalida')
"""
