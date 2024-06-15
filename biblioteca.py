import tkinter as tk
from tkinter import messagebox

class DigitalLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Digital")

        # Lista inicial de libros (simulación de una base de datos en memoria)
        self.books = [
            {"title": "Introducción a la Programación", "author": "John Doe", "subject": "Programación"},
            {"title": "Álgebra Lineal", "author": "Jane Smith", "subject": "Matemáticas"},
            {"title": "Historia del Mundo Contemporáneo", "author": "Alan Turing", "subject": "Historia"},
            {"title": "Química Básica", "author": "Marie Curie", "subject": "Química"},
            {"title": "Introducción a la Economía", "author": "Adam Smith", "subject": "Economía"},
            {"title": "Cálculo Avanzado", "author": "Isaac Newton", "subject": "Matemáticas"},
            {"title": "Introducción a la Física", "author": "Albert Einstein", "subject": "Física"},
            {"title": "Biología Molecular", "author": "Rosalind Franklin", "subject": "Biología"},
            {"title": "Literatura Universal", "author": "William Shakespeare", "subject": "Literatura"},
            {"title": "Ingeniería de Software", "author": "Linus Torvalds", "subject": "Programación"},
            {"title": "Introducción a la Psicología", "author": "Sigmund Freud", "subject": "Psicología"},
            {"title": "Diseño Gráfico Digital", "author": "Paul Rand", "subject": "Diseño"}
        ]

        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y campo de entrada para filtrar por materia
        self.subject_label = tk.Label(self.root, text="Materia:")
        self.subject_label.grid(row=0, column=0, padx=10, pady=5)

        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.grid(row=0, column=1, padx=10, pady=5)

        self.filter_button = tk.Button(self.root, text="Filtrar", command=self.filter_books)
        self.filter_button.grid(row=0, column=2, padx=10, pady=5)

        # Lista para mostrar libros
        self.books_listbox = tk.Listbox(self.root, width=50, height=10)
        self.books_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        # Botones para leer y agregar libros
        self.read_button = tk.Button(self.root, text="Leer Libro", command=self.read_book)
        self.read_button.grid(row=2, column=0, padx=10, pady=5)

        self.add_button = tk.Button(self.root, text="Agregar Libro", command=self.add_book)
        self.add_button.grid(row=2, column=1, padx=10, pady=5)

        # Mostrar todos los libros al iniciar la aplicación
        self.show_all_books()

    def show_all_books(self):
        self.books_listbox.delete(0, tk.END)
        for book in self.books:
            book_info = f"{book['title']} - {book['author']} ({book['subject']})"
            self.books_listbox.insert(tk.END, book_info)

    def filter_books(self):
        subject = self.subject_entry.get().strip().capitalize()
        if subject:
            filtered_books = [book for book in self.books if book['subject'].lower() == subject.lower()]
            if filtered_books:
                self.books_listbox.delete(0, tk.END)
                for book in filtered_books:
                    book_info = f"{book['title']} - {book['author']} ({book['subject']})"
                    self.books_listbox.insert(tk.END, book_info)
            else:
                messagebox.showinfo("No encontrado", f"No se encontraron libros de {subject}")
        else:
            self.show_all_books()

    def read_book(self):
        selected_index = self.books_listbox.curselection()
        if selected_index:
            selected_book = self.books[selected_index[0]]
            messagebox.showinfo("Leyendo Libro", f"Abriendo {selected_book['title']} para lectura...")
            # Aquí podrías implementar la lógica para abrir el libro para lectura (ej. abrir un archivo PDF, mostrar contenido en una ventana, etc.)
        else:
            messagebox.showwarning("Selecciona un libro", "Por favor, selecciona un libro de la lista.")

    def add_book(self):
        # Aquí podrías implementar una ventana emergente para que el usuario ingrese los detalles del nuevo libro
        messagebox.showinfo("Funcionalidad no implementada", "La funcionalidad para agregar libros aún no está implementada.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalLibraryApp(root)
    root.mainloop()
