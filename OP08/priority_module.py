import tkinter as tk

def add_priority_menu(root):
    """
    Создает выпадающее меню для выбора приоритета.
    Возвращает переменную StringVar для хранения выбранного приоритета.
    """
    priority_var = tk.StringVar(value="Низкий")  # Значение по умолчанию
    priority_menu = tk.OptionMenu(root, priority_var, "Низкий", "Средний", "Высокий")
    priority_menu.pack(pady=5)
    return priority_var

def add_task_with_priority(task_listBox, task, priority):
    """
    Добавляет задачу в список с указанием приоритета.
    """
    task_listBox.insert(tk.END, f"[{priority}] {task}")