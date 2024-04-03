import re
import math
from tkinter import *
from tkinter import ttk


def read_text_file(file_path="data.kt"):
    try:
        with open(file_path, 'r') as file:
            txt = file.read()
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    return txt


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


regex1 = r"(?<=val|var)+\s+[a-zA-Z]+\s*(?=[\:=]*)"   # переменные
regex2 = r"(?<=\()+\s*[a-zA-Z1-9\"._]+\s*(?=\)*)"  # параметры функций

regex3 = r"\s*(\+|-|\*|\/|%|==|!=|>|<|>=|<=|=|\+=|-=|\*=|\/=|%=|&&|\|\||!|\+\+|--|\.\.|\.|\(\)|\)|\(|if|for|when|while|do|\[.+\])(?=\s*)"  # операторы
regex4 = r"\s*[a-zA-ZА-я\w\d<>?\t\n\r]+\([\.\s\d\w\s,\"\'=.:!?\[\]\n\r\t]*\)(?=\s*)"  # функции

text = read_text_file()

result1 = count_occurrences(regex1, regex2, text)
result2 = count_occurrences(regex3, regex4, text)

result1["Итого"] = sum(result1.values())
result2["Итого"] = sum(result2.values())

n = len(result1) + len(result2)
print(f"Словарь программы. n = {n}")

N = sum(result1.values()) + sum(result2.values())
print(f"Длина программы. N = {N}")

V = N*math.log(n, 2)
print(f"Объем программы. V = {int(V)}")

root1 = Tk()
root1.title("")
root1.geometry("1050x750")
root1.rowconfigure(index=0, weight=1)
root1.columnconfigure(index=0, weight=1)

tree1 = ttk.Treeview(columns=["operands", "number"], show="headings")
tree1.grid(row=0, column=0, sticky="nsew")


tree1.heading("operands", text="Операнд")
tree1.heading("number", text="Количество вхождений")

tree1.column("#1", stretch=NO, width=300)
tree1.column("#2", stretch=NO, width=200)

for item in result1.items():
    tree1.insert("", END, values=item)

scrollbar1 = ttk.Scrollbar(orient=VERTICAL, command=tree1.yview)
tree1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.grid(row=0, column=1, sticky="ns")


tree2 = ttk.Treeview(columns=["operators", "number"], show="headings")
tree2.grid(row=0, column=2, sticky="nsew")

tree2.heading("operators", text="Оператор")
tree2.heading("number", text="Количество вхождений")

tree2.column("#1", stretch=NO, width=300)
tree2.column("#2", stretch=NO, width=200)

for item in result2.items():
    tree2.insert("", END, values=item)

scrollbar2 = ttk.Scrollbar(orient=VERTICAL, command=tree2.yview)
tree2.configure(yscrollcommand=scrollbar2.set)
scrollbar2.grid(row=0, column=3, sticky="ns")

root1.mainloop()
