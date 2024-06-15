import tkinter as tk
from tkinter import ttk
import webbrowser

class GoogleSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscador en Google")
        self.root.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12, "bold"))
        style.map("TButton", background=[("active", "#45a049")])
        style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 11))
        style.configure("TEntry", font=("Helvetica", 11))

        frame = ttk.Frame(self.root, padding=(20, 10))
        frame.pack(fill=tk.BOTH, expand=True)

        self.search_label = ttk.Label(frame, text="Buscar en Google:")
        self.search_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.search_entry = ttk.Entry(frame, width=30)
        self.search_entry.grid(row=0, column=1, padx=10, pady=5)

        self.search_button = ttk.Button(frame, text="Buscar", command=self.search_google)
        self.search_button.grid(row=1, column=0, columnspan=2, pady=10)

    def search_google(self):
        query = self.search_entry.get()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
        else:
            tk.messagebox.showwarning("Entrada inválida", "Por favor, ingrese una consulta")

if __name__ == "__main__":
    root = tk.Tk()
    app = GoogleSearchApp(root)
    root.mainloop()
