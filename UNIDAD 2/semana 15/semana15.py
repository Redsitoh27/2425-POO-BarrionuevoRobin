import tkinter as tk
from tkinter import messagebox
import json
from typing import List, Dict, TextIO, cast

# Archivo donde se guardarán las tareas
TASKS_FILE = "tasks.json"

def load_tasks() -> List[Dict[str, bool]]:
    """Carga las tareas desde un archivo JSON."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks() -> None:
    """Guarda las tareas en un archivo JSON sin warnings."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, cast(TextIO, file), ensure_ascii=False)  # Corrección del warning

def add_task(event=None) -> None:
    """Añade una nueva tarea a la lista."""
    task = entry_task.get().strip()
    if task:
        tasks.append({"task": task, "completed": False})
        update_listbox()
        save_tasks()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def mark_completed() -> None:
    """Marca una tarea como completada."""
    selected_items = listbox_tasks.curselection()
    if not selected_items:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")
        return

    selected_index = selected_items[0]
    tasks[selected_index]["completed"] = not tasks[selected_index]["completed"]
    update_listbox()
    save_tasks()

def delete_task() -> None:
    """Elimina una tarea seleccionada."""
    selected_items = listbox_tasks.curselection()
    if not selected_items:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")
        return

    selected_index = selected_items[0]
    del tasks[selected_index]
    update_listbox()
    save_tasks()

def update_listbox() -> None:
    """Actualiza la lista de tareas en la interfaz gráfica."""
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        display_text = f"✓ {task['task']}" if task["completed"] else f"✗ {task['task']}"
        listbox_tasks.insert(tk.END, display_text)

# Cargar las tareas guardadas
tasks: List[Dict[str, bool]] = load_tasks()

# Crear ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Estilos
frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
frame.pack(pady=10)

entry_task = tk.Entry(frame, width=40, font=("Arial", 12))
entry_task.pack(side=tk.LEFT, padx=5)
entry_task.bind("<Return>", add_task)

btn_add = tk.Button(frame, text="Añadir", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 10))
btn_add.pack(side=tk.RIGHT)

listbox_tasks = tk.Listbox(root, width=50, height=15, font=("Arial", 12), selectbackground="#ccc")
listbox_tasks.pack(pady=10)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack()

btn_complete = tk.Button(btn_frame, text="Marcar como Completada", command=mark_completed, bg="#2196F3", fg="white", font=("Arial", 10))
btn_complete.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(btn_frame, text="Eliminar Tarea", command=delete_task, bg="#F44336", fg="white", font=("Arial", 10))
btn_delete.pack(side=tk.RIGHT, padx=5)

# Cargar tareas en la lista
update_listbox()

# Ejecutar la aplicación
root.mainloop()
