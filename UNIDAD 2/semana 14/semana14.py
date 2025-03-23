import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame para entrada de datos
        self.frame_inputs = tk.Frame(self.root)
        self.frame_inputs.pack(pady=10)

        tk.Label(self.frame_inputs, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_inputs, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.frame_inputs)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_inputs)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar evento
        self.add_button = tk.Button(self.frame_inputs, text="Agregar Evento", command=self.agregar_evento)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame para lista de eventos
        self.frame_list = tk.Frame(self.root)
        self.frame_list.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Botón para eliminar evento
        self.delete_button = tk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.delete_button.pack(pady=5)

        # Botón para salir
        self.exit_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")
            if confirmar:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
