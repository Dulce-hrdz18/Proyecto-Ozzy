import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class SchoolAppointmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Citas Escolares")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        self.appointments = []

        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada
        self.name_label = ttk.Label(self.root, text="Nombre del Estudiante:", background="#f0f0f0", foreground="#333")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        self.date_label = ttk.Label(self.root, text="Fecha (dd/mm/aaaa):", background="#f0f0f0", foreground="#333")
        self.date_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.date_entry = ttk.Entry(self.root)
        self.date_entry.grid(row=1, column=1, padx=10, pady=10, sticky="we")

        self.time_label = ttk.Label(self.root, text="Hora (HH:MM):", background="#f0f0f0", foreground="#333")
        self.time_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.time_entry = ttk.Entry(self.root)
        self.time_entry.grid(row=2, column=1, padx=10, pady=10, sticky="we")

        # Botón para agendar cita
        self.add_button = ttk.Button(self.root, text="Agregar Cita", command=self.add_appointment)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Lista para mostrar citas
        self.appointments_listbox = tk.Listbox(self.root, width=50)
        self.appointments_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configurar el grid para que se expanda con la ventana
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

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
    app = SchoolAppointmentApp(root)
    root.mainloop()
