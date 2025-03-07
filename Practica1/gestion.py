''' Integrantes: 
    Maria de los Angeles Flores
    Luis Alejandro Gordillo
    Leslie Alejandra Guerrero 
    Diana Marcela Patiño
    
  ''' 
import tkinter as tk
from tkinter import messagebox
#from Persona import Persona
from Estudiante import Estudiante
from docente import Docente
from curso import Curso

class GestionUniversitaria:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Universitaria")
        self.root.geometry("400x300")
        
        self.estudiantes = []
        self.docentes = []
        self.cursos = []
        
        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(pady=10)
        
        tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.entry_nombre = tk.Entry(frame, width=30)
        self.entry_nombre.grid(row=0, column=1)
        
        tk.Label(frame, text="Edad:").grid(row=1, column=0, sticky="w")
        self.entry_edad = tk.Entry(frame, width=30)
        self.entry_edad.grid(row=1, column=1)
        
        tk.Label(frame, text="Dirección:").grid(row=2, column=0, sticky="w")
        self.entry_direccion = tk.Entry(frame, width=30)
        self.entry_direccion.grid(row=2, column=1)
        
        tk.Label(frame, text="Curso/Código:").grid(row=3, column=0, sticky="w")
        self.entry_curso = tk.Entry(frame, width=30)
        self.entry_curso.grid(row=3, column=1)
        
        button_frame = tk.Frame(root, padx=10, pady=5)
        button_frame.pack()
        
        tk.Button(button_frame, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=0, column=0, padx=5, pady=2)
        tk.Button(button_frame, text="Agregar Docente", command=self.agregar_docente).grid(row=0, column=1, padx=5, pady=2)
        tk.Button(button_frame, text="Agregar Curso", command=self.agregar_curso).grid(row=0, column=2, padx=5, pady=2)
        
        tk.Button(button_frame, text="Mostrar Estudiantes", command=self.mostrar_estudiantes).grid(row=1, column=0, padx=5, pady=2)
        tk.Button(button_frame, text="Mostrar Docentes", command=self.mostrar_docentes).grid(row=1, column=1, padx=5, pady=2)
        tk.Button(button_frame, text="Mostrar Cursos", command=self.mostrar_cursos).grid(row=1, column=2, padx=5, pady=2)
    
    def agregar_estudiante(self):
        nombre = self.entry_nombre.get().strip()
        edad = self.entry_edad.get()
        direccion = self.entry_direccion.get()
        curso_nombre = self.entry_curso.get().strip()
        
        if not nombre or not curso_nombre:
            messagebox.showerror("Error", "El nombre y el curso no pueden estar vacíos")
            return
        
        curso_existente = next((c for c in self.cursos if c.get_nombre() == curso_nombre), None)
        
        if not curso_existente:
            messagebox.showerror("Error", "El curso ingresado no existe. Agregue el curso primero.")
            return
        
        estudiante = Estudiante(nombre, edad, direccion, curso_existente)
        self.estudiantes.append(estudiante)
        messagebox.showinfo("Éxito", f"Estudiante agregado exitosamente:\n{estudiante}")
    
    def agregar_docente(self):
        nombre = self.entry_nombre.get().strip()
        edad = self.entry_edad.get()
        direccion = self.entry_direccion.get()
        
        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío")
            return
        
        docente = Docente(nombre, edad, direccion)
        self.docentes.append(docente)
        messagebox.showinfo("Éxito", f"Docente agregado exitosamente:\n{docente}")
    
    def agregar_curso(self):
        nombre = self.entry_nombre.get().strip()
        codigo = self.entry_curso.get().strip()
        
        if not nombre or not codigo:
            messagebox.showerror("Error", "El nombre y el código del curso no pueden estar vacíos")
            return
        
        curso = Curso(nombre, codigo)
        self.cursos.append(curso)
        messagebox.showinfo("Éxito", f"Curso agregado exitosamente:\n{curso}")
    
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            messagebox.showinfo("Estudiantes", "No hay estudiantes registrados")
            return
        
        info = "\n".join(str(e) for e in self.estudiantes)
        messagebox.showinfo("Estudiantes", info)
    
    def mostrar_docentes(self):
        if not self.docentes:
            messagebox.showinfo("Docentes", "No hay docentes registrados")
            return
        
        info = "\n".join(str(d) for d in self.docentes)
        messagebox.showinfo("Docentes", info)
    
    def mostrar_cursos(self):
        if not self.cursos:
            messagebox.showinfo("Cursos", "No hay cursos registrados")
            return
        
        info = "\n".join(str(c) for c in self.cursos)
        messagebox.showinfo("Cursos", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionUniversitaria(root)
    root.mainloop()