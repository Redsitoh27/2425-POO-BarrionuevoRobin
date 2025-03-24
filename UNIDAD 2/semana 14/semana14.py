import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get().strip()
    descripcion = entry_descripcion.get().strip()
    if fecha and hora and descripcion:
        tree.insert("", "end", values=(str(fecha), str(hora), str(descripcion)))
        entry_fecha.set_date(None)  # Se limpia el campo de fecha
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.")

def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirmar = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar el evento seleccionado?")
        if confirmar:
            tree.delete(selected_item[0])  # Se toma el primer elemento de la selección
    else:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")

# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para la lista de eventos
tree_frame = ttk.Frame(root)
tree_frame.pack(pady=10)

tree = ttk.Treeview(tree_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame para los campos de entrada y botones
entry_frame = ttk.Frame(root)
entry_frame.pack(pady=10)

ttk.Label(entry_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(entry_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(entry_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
entry_hora = ttk.Entry(entry_frame)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(entry_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = ttk.Entry(entry_frame)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Agregar Evento", command=agregar_evento).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Eliminar Evento", command=eliminar_evento).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

root.mainloop()

