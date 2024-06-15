import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Configurar la conexión a la base de datos MySQL
def connect_to_db():
#    return mysql.connector.connect
        BD=mysql.connector.connect(user="root", password="", host="localhost", database="usuarios_db", port="3306")
        print(BD)
        Insercion_de_usuario= BD.cursor()
        sql="""INSERT INTO usuario (Usuario, Contraseña) VALUES  ('{}','{}')""".format(entry_username.get(),entry_password.get())
        Insercion_de_usuario.execute(sql)
        BD.commit()

# Función para verificar las credenciales del usuario
def verificar_credenciales():
        BD=mysql.connector.connect(user="root", password="", host="localhost", database="usuarios_db", port="3306")
        print(BD)
        busqueda_de_usuario= BD.cursor()
        busqueda_de_usuario.execute("SELECT * FROM usuario WHERE Usuario='"+entry_username.get()+"' and Contraseña='"+entry_password.get()+"'")
        if(busqueda_de_usuario.fetchall()):
            messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido!")
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Inicio de Sesión")

tk.Label(root, text="Nombre de Usuario:").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Contraseña:").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

btn_login = tk.Button(root, text="Iniciar Sesión", command=verificar_credenciales)
btn_login.grid(row=2, columnspan=2)

btn_register = tk.Button(root, text="Registrarse", command=connect_to_db)
btn_register.grid(row=3, columnspan=2)

root.mainloop()