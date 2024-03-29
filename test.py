import tkinter as tk
from tkinter import ttk

# Создание главного окна
root = tk.Tk()

# Создание первой таблицы
treeview1 = ttk.Treeview(root)
treeview1["columns"] = ("column1", "column2")
treeview1.heading("column1", text="Заголовок 1")
treeview1.heading("column2", text="Заголовок 2")
treeview1.insert("", "end", text="Ряд 1", values=("Значение 1", "Значение 2"))
treeview1.insert("", "end", text="Ряд 2", values=("Значение 3", "Значение 4"))
treeview1.pack()

# Создание второй таблицы
treeview2 = ttk.Treeview(root)
treeview2["columns"] = ("column1", "column2")
treeview2.heading("column1", text="Заголовок 1")
treeview2.heading("column2", text="Заголовок 2")
treeview2.insert("", "end", text="Ряд 1", values=("Значение 1", "Значение 2"))
treeview2.insert("", "end", text="Ряд 2", values=("Значение 3", "Значение 4"))
treeview2.pack()

# Запуск главного цикла
root.mainloop()