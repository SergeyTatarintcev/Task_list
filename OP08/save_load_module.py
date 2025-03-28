import tkinter as tk
import json

def save_tasks(task_listBox):
    """
    Сохраняет задачи из Listbox в файл tasks.json.
    """
    tasks = task_listBox.get(0, tk.END)  # Получаем все задачи из Listbox
    with open("tasks.json", "w") as file:
        json.dump(list(tasks), file)

def load_tasks(task_listBox):
    """
    Загружает задачи из файла tasks.json в Listbox.
    """
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_listBox.insert(tk.END, task)  # Добавляем задачи в Listbox
    except FileNotFoundError:
        pass  # Если файл не существует, ничего не делаем