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
    file_path = filedialog.askopenfilename(filetypes=[("Kotlin Files", (".kt", ".kts")),
                                                      ("Text Files", "*.txt"),
                                                      ("All Files", "*.*")])
    if file_path:
        text.delete("1.0", END)
        text.insert(END, read_text_file(file_path))


def count_occurrences(reg, txt):
    matches = re.findall(reg, txt)  # Находим все вхождения по регулярному выражению
    occurrence_count = {}  # Словарь для подсчета количества вхождений
    if reg == r"(\bwhen\b.+{(.|\n|\t|\r)*})":
        if " " in matches:
            matches.remove(" ")

    for match in matches:
        if match in occurrence_count:
            occurrence_count[match] += 1
        else:
            occurrence_count[match] = 1

    return occurrence_count


regex1 = r"\b(else\s+if|if(?=.+else)*|for|while)\b"  # условные операторы
regex2 = r"(\bwhen\b.+{(.|\n|\t|\r)*})"  # оператор when


def calculate_metrics():
    global res_count_cond_operators, result2
    text_content = text.get("1.0", END)
    res_count_cond_operators = count_occurrences(regex1, text_content)
    res_count_cond_operators += count_occurrences(regex2, text_content)






    # n = len(result1) + len(result2)
    # output_text = f"Словарь программы. n = {len(result1)} + {len(result2)} = {n}\n"
    # N = sum(result1.values()) + sum(result2.values())
    # output_text += f"Длина программы. N = {sum(result1.values())} + {sum(result2.values())} = {N}\n"
    # V = N * math.log(n, 2)
    # output_text += f"Объем программы. V = {N}*log2({n}) = {int(V)}"
    # result1["Итого"] = sum(result1.values())
    # result2["Итого"] = sum(result2.values())
    # output.config(state='normal')
    # output.delete("1.0", END)
    # output.insert(END, output_text)
    # output.config(state='disabled')



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