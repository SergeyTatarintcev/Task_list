import tkinter as tk

def add_filter_buttons(root, task_listBox):
    def filter_tasks(priority):
        task_listBox.delete(0, tk.END)
        for task in all_tasks:
            if f"[{priority}]" in task:
                task_listBox.insert(tk.END, task)

    all_tasks = []

    def save_all_tasks():
        nonlocal all_tasks
        all_tasks = task_listBox.get(0, tk.END)


    tk.Button(root, text="Фильтр: Низкий", command=lambda: filter_tasks("Низкий")).pack(pady=5)
    tk.Button(root, text="Фильтр: Средний", command=lambda: filter_tasks("Средний")).pack(pady=5)
    tk.Button(root, text="Фильтр: Высокий", command=lambda: filter_tasks("Высокий")).pack(pady=5)
    tk.Button(root, text="Показать все задачи",
              command=lambda: task_listBox.delete(0, tk.END) or [task_listBox.insert(tk.END, task) for task in
                                                                 all_tasks]).pack(pady=5)

    task_listBox.bind("<<ListboxSelect>>", lambda event: save_all_tasks())