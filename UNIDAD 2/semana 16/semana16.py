import tkinter as tk
from tkinter import messagebox
import json
import os

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        self.root.bind('<Escape>', lambda e: self.root.quit())

        self.tasks = []

        self.load_tasks()

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10, padx=10, fill="x")
        self.entry.bind('<Return>', lambda event: self.add_task())

        self.frame_buttons = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_buttons.pack(pady=5)

        self.add_button = tk.Button(self.frame_buttons, text="Añadir", command=self.add_task, bg="#4CAF50", fg="white", width=10)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(self.frame_buttons, text="Completar", command=self.complete_task, bg="#2196F3", fg="white", width=10)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.frame_buttons, text="Eliminar", command=self.delete_task, bg="#f44336", fg="white", width=10)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.listbox = tk.Listbox(self.root, font=("Arial", 12), selectbackground="#c0c0c0", activestyle='none')
        self.listbox.pack(padx=10, pady=10, fill="both", expand=True)
        self.listbox.bind('<c>', lambda event: self.complete_task())
        self.listbox.bind('<C>', lambda event: self.complete_task())
        self.listbox.bind('<d>', lambda event: self.delete_task())
        self.listbox.bind('<D>', lambda event: self.delete_task())

        self.update_listbox()

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.entry.delete(0, tk.END)
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")

    def complete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task['text']
            if task['completed']:
                display_text = "✔️ " + display_text
            self.listbox.insert(tk.END, display_text)

    def save_tasks(self):
        with open("tareas.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists("tareas.json"):
            with open("tareas.json", "r") as f:
                self.tasks = json.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
