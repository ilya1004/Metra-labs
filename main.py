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
    matches = re.findall(reg, txt)
    occurrence_count = {}
    if reg == r"(\bwhen\b.+{(.|\n|\t|\r)*})":
        if "\n" in matches:
            matches.remove("\n")
        if " " in matches:
            matches.remove(" ")

    for match in matches:
        if match in occurrence_count:
            occurrence_count[match] += 1
        else:
            occurrence_count[match] = 1

    return occurrence_count


def max_nesting_level(code):
    max_depth = 0
    current_depth = 0
    when_depth = -1
    in_when = False
    in_elif = False
    for line in code.split('\n'):
        stripped = line.strip()
        if (stripped.startswith('if') or stripped.find('else if') != -1 or
                (stripped.find('else') != -1 and in_when is True) or stripped.startswith("do")):
            if stripped.find('else if') != -1:
                in_elif = True
            if stripped.find('else') != -1 and in_when is True:
                when_depth += 1
                max_depth = max(max_depth, when_depth - 1)
                continue
            current_depth += 1
            max_depth = max(max_depth, current_depth)

        elif stripped.find("when") != -1:
            in_when = True

        elif stripped.find("->") != -1 and in_when:
            when_depth += 1
            current_depth += 1
            max_depth = max(max_depth, when_depth - 1)

        elif stripped.startswith("for") or stripped.startswith("while"):
            current_depth += 1
            max_depth = max(max_depth, current_depth)

        elif stripped.startswith("}") and stripped.find("else") == -1:
            if current_depth > 0:
                current_depth -= 1

            if in_elif:
                current_depth -= 1
                in_elif = False

            if in_when:
                in_when = False
                current_depth -= when_depth - 1
                when_depth = -1

    return max_depth - 1


regex1 = r"\b(else\s+if|if(?=.+else)*|for|while)\b"  # условные операторы
regex2 = r"(\bwhen\b.+{(.|\n|\t|\r)*})"  # оператор when
regex3 = r"\s*(,|->|\+|-|\*|\/|%|==|!=|>|<|>=|<=|=|\+=|-=|\*=|\/=|%=|&&|\|\||!|\+\+|--|\.\.|\.|\(.+\)|else\s+if|if|for|when|while|return|throw|!=|do|\[.+\])(?=\s*)"  # все операторы


def calculate_metrics():
    text_content = text.get("1.0", END)

    print(max_nesting_level(text_content))

    res_count_cond_operators = count_occurrences(regex1, text_content)
    res_count_cond_operators.update(count_occurrences(regex2, text_content))
    res_count_all_operators = count_occurrences(regex3, text_content)

    output_text = f"Метрика Джилба.\n"
    output_text += f"Количество условных операторов (CL): {sum(res_count_cond_operators.values())}\n"
    output_text += f"Общее количество операторов: {sum(res_count_all_operators.values())}\n"
    output_text += (f"Насыщенность программы условными операторыми (cl): "
                    f"{sum(res_count_cond_operators.values()) / sum(res_count_all_operators.values())}\n")

    output.config(state='normal')
    output.delete("1.0", END)
    output.insert(END, output_text)
    output.config(state='disabled')


if __name__ == "__main__":

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

    root1.mainloop()