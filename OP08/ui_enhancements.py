def mark_task_with_strikethrough(task_listBox, selected_task):
    """
    Отмечает задачу как выполненную: меняет цвет фона и добавляет символы зачёркивания.
    """
    task_text = task_listBox.get(selected_task)  # Получаем текст задачи
    if not task_text.startswith("~"):  # Добавляем символы зачёркивания только один раз
        task_listBox.delete(selected_task)  # Удаляем старую задачу
        task_listBox.insert(selected_task, f"~{task_text}~")  # Добавляем задачу с зачёркиванием
    task_listBox.itemconfig(selected_task, bg="green", fg="white")  # Меняем цвет фона и текста