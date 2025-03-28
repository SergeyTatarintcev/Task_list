import tkinter as tk
from priority_module import add_priority_menu, add_task_with_priority
from save_load_module import save_tasks, load_tasks
from ui_enhancements import mark_task_with_strikethrough
from tooltips_module import add_tooltips
from appearance_module import apply_appearance_settings
from filter_module import add_filter_buttons

# Проверка загрузки модулей
try:
    print("tooltips_module загружен успешно!")
except ImportError as e:
    print(f"Ошибка при импорте tooltips_module: {e}")

try:
    print("appearance_module загружен успешно!")
except ImportError as e:
    print(f"Ошибка при импорте appearance_module: {e}")

try:
    print("datetime_module загружен успешно!")
except ImportError as e:
    print(f"Ошибка при импорте datetime_module: {e}")

try:
    print("filter_module загружен успешно!")
except ImportError as e:
    print(f"Ошибка при импорте filter_module: {e}")
# Основные функции
def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        mark_task_with_strikethrough(task_listBox, selected_task)
# Создание главного окна
root = tk.Tk()
root.title("Task list")
root.configure(background="#FAFAFA")  # Фон окна
root.geometry("800x1000")
root.resizable(False, False)
# Применяем улучшенный внешний вид
apply_appearance_settings(root)
# Получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Вычисляем координаты для центрирования окна
x = (screen_width // 2) - (600 // 2)
y = (screen_height // 2) - (800 // 2)

# Устанавливаем положение окна
root.geometry(f"600x800+{x}+{y}")
# Текстовые метки
text1 = tk.Label(root, text="Введите вашу задачу:", bg="#D3D3D3")
text1.pack(pady=10)

# Поле ввода задачи
task_entry = tk.Entry(root, width=30, background="#F0F8FF", fg="#000000")
task_entry.pack(pady=10)

# Добавляем выпадающее меню для приоритетов
priority_var = add_priority_menu(root)

# Кнопки
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=10)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=10)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=10)

# Дополнительные кнопки для сохранения и загрузки задач
save_button = tk.Button(root, text="Сохранить задачи", command=lambda: save_tasks(task_listBox))
save_button.pack(pady=5)

load_button = tk.Button(root, text="Загрузить задачи", command=lambda: load_tasks(task_listBox))
load_button.pack(pady=5)

# Список задач
text2 = tk.Label(root, text="Список задач:", bg="#D3D3D3")
text2.pack(pady=10)

task_listBox = tk.Listbox(root, height=10, width=50, background="#F0F8FF")
task_listBox.pack(pady=10)

# Добавляем всплывающие подсказки
add_tooltips(root, add_task_button, delete_button, mark_button, save_button, load_button)

# Фильтрация задач
add_filter_buttons(root, task_listBox)

# Запуск программы
root.mainloop()