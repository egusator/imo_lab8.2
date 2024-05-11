import tkinter as tk

window = tk.Tk()
window.title("8.1")
window.geometry('520x300')
window.maxsize(520, 300)
window.resizable(0, 1)

question_label = tk.Label(window, text="Задайте вопрос:", font=("Arial", 20))
question_label.pack()


name_entry = tk.Entry(font=("Arial", 16))
name_entry.pack()

answer_label = tk.Label(window, text="...", font = ("Arial", 18))
answer_label.pack()

responses = [
    "Да",
    "Нет",
    "Возможно",
    "Попробуй снова позже",
    "Не могу предсказать",
    "Вероятно",
    "Сомнительно",
    "Без сомнения",
    "Спроси позже",
    "Не стоит на это надеяться",
    "Конечно",
    "Ни в коем случае",
    "Скорее всего",
    "Знаки указывают на это",
    "Может быть",
    "Определенно нет",
    "Может быть, да",
    "Мой ответ — нет",
    "Мой ответ — да",
    "Не задавай этот вопрос"
]

import random, math

def button_clicked():

    random_value = random.random()

    index = math.ceil(random_value*20)
    index = index - 1 if index == 20 else index
    answer_label.configure(text=responses[index])



button = tk.Button(window,
                   text="Получить ответ",
                   command=button_clicked,
                   activebackground="blue",
                   activeforeground="white",
                   font=("Arial", 18))

button.place(x = 160, y = 130)

window.mainloop()