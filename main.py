import re
import math
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def read_text_file(file_path="data.kt"):
    try:
        with open(file_path, 'r') as file:
            txt = file.read()
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    return txt


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Kotlin Files", ".kt"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        text.delete("1.0", END)
        text.insert(END, read_text_file(file_path))


def count_occurrences(reg1, reg2, txt):
    matches = re.findall(reg1, txt)  # Находим все вхождения по регулярному выражению
    matches.extend(re.findall(reg2, txt))
    occurrence_count = {}  # Словарь для подсчета количества вхождений
    matches = [i.strip() for i in matches]
    for match in matches:
        if match in occurrence_count:
            occurrence_count[match] += 1
        else:
            occurrence_count[match] = 1

    return occurrence_count


def calculate_metrics():
    global result1, result2
    text_content = text.get("1.0", END)
    result1 = count_occurrences(regex1, regex2, text_content)
    result2 = count_occurrences(regex3, regex4, text_content)
    result1["Итого"] = sum(result1.values())
    result2["Итого"] = sum(result2.values())
    n = len(result1) + len(result2)
    output_text = f"Словарь программы. n = {n}\n"
    N = sum(result1.values()) + sum(result2.values())
    output_text += f"Длина программы. N = {N}\n"
    V = N * math.log(n, 2)
    output_text += f"Объем программы. V = {int(V)}"
    output.config(state='normal')
    output.delete("1.0", END)
    output.insert(END, output_text)
    output.config(state='disabled')
    update_treeview()


def update_treeview():
    tree1.delete(*tree1.get_children())
    for item in result1.items():
        tree1.insert("", END, values=item)

    tree2.delete(*tree2.get_children())
    for item in result2.items():
        tree2.insert("", END, values=item)


regex1 = r"(?<=val|var)+\s+[a-zA-Z]+\s*(?=[\:=]*)"   # переменные
regex2 = r"(?<=\()+\s*[a-zA-Z1-9\"._]+\s*(?=\)*)"  # параметры функций

regex3 = r"\s*(\+|-|\*|\/|%|==|!=|>|<|>=|<=|=|\+=|-=|\*=|\/=|%=|&&|\|\||!|\+\+|--|\.\.|\.|\(\)|\)|\(|if|for|when|while|do|\[.+\])(?=\s*)"  # операторы
regex4 = r"\s*[a-zA-ZА-я\w\d<>?\t\n\r]+\([\.\s\d\w\s,\"\'=.:!?\[\]\n\r\t]*\)(?=\s*)"  # функции

root1 = Tk()
root1.title("")
root1.geometry("1050x750")
root1.rowconfigure(index=0, weight=1)
root1.columnconfigure(index=0, weight=1)

frame = Frame(root1)
frame.pack(pady=10)

select_button = Button(frame, text="Выбрать файл", command=open_file)
select_button.pack(side=LEFT)

calculate_button = Button(frame, text="Рассчитать", command=calculate_metrics)
calculate_button.pack(side=LEFT)

text_frame = Frame(root1)
text_frame.pack(fill=BOTH, expand=True)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(text_frame, height=15, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH, expand=True)

scrollbar.config(command=text.yview)

output_frame = Frame(root1)
output_frame.pack(fill=BOTH, expand=True)

output_label = Label(output_frame, text="Результат:")
output_label.pack()

output = Text(output_frame, height=1)
output.pack(fill=BOTH, expand=True)
output.config(state='disabled')


tree_frame = Frame(root1)
tree_frame.pack(fill=BOTH, expand=True)

tree1 = ttk.Treeview(tree_frame, columns=["operands", "number"], show="headings", height=15)
tree1.grid(row=0, column=0, sticky="nsew")
tree1.heading("operands", text="Операнд")
tree1.heading("number", text="Количество вхождений")
tree1.column("#1", stretch=NO, width=300)
tree1.column("#2", stretch=NO, width=200)

scrollbar1 = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree1.yview)
tree1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.grid(row=0, column=1, sticky="ns")

tree2 = ttk.Treeview(tree_frame, columns=["operators", "number"], show="headings")
tree2.grid(row=0, column=2, sticky="nsew")
tree2.heading("operators", text="Оператор")
tree2.heading("number", text="Количество вхождений")
tree2.column("#1", stretch=NO, width=300)
tree2.column("#2", stretch=NO, width=200)

scrollbar2 = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree2.yview)
tree2.configure(yscrollcommand=scrollbar2.set)
scrollbar2.grid(row=0, column=3, sticky="ns")

root1.mainloop()