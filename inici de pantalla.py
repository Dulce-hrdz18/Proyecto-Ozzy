import tkinter as tk
from tkinter import messagebox

class StartPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio")
        
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.root, text="Bienvenido al asistente Ozzy", font=("Helvetica", 18))
        label.pack(pady=20)

        start_button = tk.Button(self.root, text="Iniciar Aplicación", command=self.open_appointment_app)
        start_button.pack(pady=10)

    def open_appointment_app(self):
        self.root.destroy()  # Cierra la pantalla de inicio
        root = tk.Tk()  # Crea la ventana principal para la aplicación de citas
        app = SchoolAppointmentApp(root)
        root.mainloop()

class SchoolAppointmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Citas Escolares")
        
        self.appointments = []

        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada
        self.name_label = tk.Label(self.root, text="Nombre del Estudiante:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.date_label = tk.Label(self.root, text="Fecha (dd/mm/aaaa):")
        self.date_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        self.time_label = tk.Label(self.root, text="Hora (HH:MM):")
        self.time_label.grid(row=2, column=0, padx=10, pady=5)
        
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para agendar cita
        self.add_button = tk.Button(self.root, text="Agregar Cita", command=self.add_appointment)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Lista para mostrar citas
        self.appointments_listbox = tk.Listbox(self.root, width=50)
        self.appointments_listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def add_appointment(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        if name and date and time:
            appointment = {"name": name, "date": date, "time": time}
            self.appointments.append(appointment)
            self.update_appointments_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, complete todos los campos")

    def update_appointments_listbox(self):
        self.appointments_listbox.delete(0, tk.END)
        for appointment in self.appointments:
            appointment_str = f"{appointment['date']} {appointment['time']} - {appointment['name']}"
            self.appointments_listbox.insert(tk.END, appointment_str)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    start_page = StartPage(root)
    root.mainloop()
