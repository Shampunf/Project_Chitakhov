import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Форма FireFox")
root.geometry("500x500")
root.resizable(False, False)

topBar = tk.Frame(root, bg="#d9d9d9", height=30)
topBar.pack(fill="x")
topBar.pack_propagate(False)

tk.Label(topBar,text="Обработка формы – Mozilla Firefox",bg="#d9d9d9",fg="#333333",font=("Arial", 11, "bold")).place(relx=0.5, rely=0.5, anchor="center")

tabsBar = tk.Frame(root, bg="#e6e6e6", height=35)
tabsBar.pack(fill="x")
tabsBar.pack_propagate(False)

tk.Label(tabsBar, text="Firefox ▾", bg="#e6e6e6").pack(side="left", padx=10, pady=5)

tk.Label(tabsBar,text="Обработка формы",bg="#f2f2f2",relief="groove",padx=10).pack(side="left", pady=5)

tk.Label(tabsBar,text="+", bg="#dcdcdc",width=3,relief="groove").pack(side="left", padx=5, pady=5)

title = tk.Label(root,text="Форма регистрации пользователя",font=("Arial", 14, "bold"))
title.pack(pady=(10, 5))

frame = tk.Frame(root, padx=10, pady=10, relief="solid", borderwidth=1)
frame.pack(pady=10)

tk.Label(frame, text="Ваше имя:").grid(row=0, column=0, sticky="w")
tk.Entry(frame, width=30).grid(row=0, column=1)

tk.Label(frame, text="Пароль:").grid(row=1, column=0, sticky="w")
tk.Entry(frame, width=30).grid(row=1, column=1)

tk.Label(frame, text="Возраст:").grid(row=2, column=0, sticky="w")
tk.Entry(frame, width=30).grid(row=2, column=1)

tk.Label(frame, text="Пол:").grid(row=3, column=0, sticky="w")
tk.Radiobutton(frame, text="Мужской", value="M").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame, text="Женский", value="F").grid(row=3, column=1, sticky="e")

tk.Label(frame, text="Увлечения:").grid(row=4, column=0, sticky="w")
tk.Checkbutton(frame, text="Музыка").grid(row=4, column=1, sticky="w")
tk.Checkbutton(frame, text="Видео").grid(row=4, column=1)
tk.Checkbutton(frame, text="Рисование").grid(row=4, column=1, sticky="e")

tk.Label(frame, text="Страна:").grid(row=5, column=0, sticky="w")
ttk.Combobox(frame, values=["Россия", "Германия", "Финляндия", "Казахстан"]).grid(row=5, column=1)

tk.Label(frame, text="Город:").grid(row=6, column=0, sticky="w")
ttk.Combobox(frame, values=["Москва","Ростов-на-Дону","Нижний Новгород","Пенза", "Берлин","Мюнхен", "Хельсинки", "Алматы", "Астана","Павлодар"]).grid(row=6, column=1)

tk.Label(frame, text="Кратко о себе:").grid(row=7, column=0, sticky="nw")
text = tk.Text(frame, width=30, height=4)
text.tag_config("hint", foreground="#9d9d9d")
text.insert("1.0", "Краткая информация о ваших увлечениях", "hint")
text.grid(row=7, column=1)

tk.Label(frame, text="Решите пример, запишите результат в поле ниже: ").grid(row=8, column=0, columnspan=2, sticky="w")
text2 = tk.Text(frame, width=30, height=1)
text2.grid(row=9, column=1)

button_row = tk.Frame(frame)
button_row.grid(row=10, column=0, columnspan=3, pady=10)

tk.Button(button_row, text="Отменить ввод").pack(side="left", padx=10)
tk.Button(button_row, text="Данные подтверждаю").pack(side="left", padx=10)

root.mainloop()