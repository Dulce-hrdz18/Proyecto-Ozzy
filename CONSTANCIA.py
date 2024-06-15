import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StudyCertificateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Constancias de Estudio")
        self.root.geometry("600x400")
        self.root.configure(bg="#BB8FCE")

        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada
        self.name_label = ttk.Label(self.root, text="Nombre del Estudiante:", background="#D5F5E3", foreground="#333")
        self.name_label.grid(row=0, column=0, padx=20, pady=30, sticky="w")
        
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=100, pady=10, sticky="we")

        self.grade_label = ttk.Label(self.root, text="Grado o Curso:", background="#D5F5E3", foreground="#333")
        self.grade_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.grade_entry = ttk.Entry(self.root)
        self.grade_entry.grid(row=1, column=1, padx=120, pady=10, sticky="we")

        self.school_label = ttk.Label(self.root, text="Nombre de la Escuela:", background="#D5F5E3", foreground="#333")
        self.school_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.school_entry = ttk.Entry(self.root)
        self.school_entry.grid(row=2, column=1, padx=150, pady=10, sticky="we")

        # Botón para generar la constancia
        self.generate_button = ttk.Button(self.root, text="Generar Constancia", command=self.generate_certificate)
        self.generate_button.grid(row=3, column=0, columnspan=5, pady=50)

    def generate_certificate(self):
        name = self.name_entry.get()
        grade = self.grade_entry.get()
        school = self.school_entry.get()

        if name and grade and school:
            content = f"Constancia de Estudios\n\nNombre del Estudiante: {name}\nGrado o Curso: {grade}\nEscuela: {school}"

            try:
                with open(f"{name}_constancia.txt", "w") as file:
                    file.write(content)
                messagebox.showinfo("Constancia Generada", f"Se ha generado la constancia para {name}")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al generar la constancia: {str(e)}")
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, complete todos los campos")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyCertificateApp(root)
    root.mainloop()
