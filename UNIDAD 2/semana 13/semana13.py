import tkinter as tk
from tkinter import messagebox


class DataApp:
    def __init__(self, rooot):
        # Configuración de la ventana principal
        self.root = rooot
        self.root.title("Granja Piscicultora Barrionuevo")  # Título de la aplicación
        self.root.geometry("400x300")  # Tamaño de la ventana

        # Etiqueta descriptiva
        self.label = tk.Label(rooot, text="Ingrese información sobre la granja:")
        self.label.pack(pady=5)

        # Campo de texto para ingresar datos
        self.entry = tk.Entry(rooot, width=40)
        self.entry.pack(pady=5)

        # Botón para agregar datos a la lista
        self.add_button = tk.Button(rooot, text="Agregar", command=self.add_data)
        self.add_button.pack(pady=5)

        # Lista para mostrar los datos ingresados
        self.data_listbox = tk.Listbox(rooot, width=50, height=10)
        self.data_listbox.pack(pady=5)

        # Botón para limpiar la lista de datos
        self.clear_button = tk.Button(rooot, text="Limpiar", command=self.clear_data)
        self.clear_button.pack(pady=5)

    def add_data(self):
        """ Agrega el dato ingresado a la lista """
        data = self.entry.get()
        if data:
            self.data_listbox.insert(tk.END, data)  # Agregar el dato a la lista
            self.entry.delete(0, tk.END)  # Limpiar el campo de texto
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese algún dato.")

    def clear_data(self):
        """ Elimina todos los datos de la lista """
        self.data_listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
