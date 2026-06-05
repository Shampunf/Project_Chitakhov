import tkinter as tk
from tkinter import ttk

# Создаем главное окно
root = tk.Tk()
root.title("Регистрационная страница электронной библиотеки")
root.geometry("650x750")

# Задаем фирменный розовый цвет фона для всего окна
BG_COLOR = "#FF9999"
root.configure(bg=BG_COLOR)

# Стили для элементов (убираем белый фон у кнопок выбора)
style = ttk.Style()
style.theme_use('clam')
style.configure("TRadiobutton", background=BG_COLOR, font=("Arial", 11))
style.configure("TCheckbutton", background=BG_COLOR, font=("Arial", 11))

# Настраиваем адаптивность колонок (чтобы левая колонка не прижималась)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# --- 1. ЗАГОЛОВКИ ---
title1 = tk.Label(root, text="Регистрационная страница электронной библиотеки",
                  font=("Arial", 14, "bold"), bg=BG_COLOR)
title1.grid(row=0, column=0, columnspan=4, pady=(15, 5), sticky="w", padx=15)

title2 = tk.Label(root, text="Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой",
                  font=("Arial", 11), bg=BG_COLOR)
title2.grid(row=1, column=0, columnspan=4, pady=(0, 15), sticky="w", padx=15)

# --- 2. ТЕКСТОВЫЕ ПОЛЯ ВВОДА (Имя, Пароль, Подтверждение) ---
labels_text = ["Введите регистрационное имя", "Введите пароль", "Подтвердите пароль"]
entries = {}

for i, label_txt in enumerate(labels_text):
    lbl = tk.Label(root, text=label_txt, font=("Arial", 11), bg=BG_COLOR)
    lbl.grid(row=2 + i, column=0, sticky="w", padx=15, pady=5)

    # Для паролей скрываем символы звездочками
    show_char = "*" if "пароль" in label_txt else None
    ent = tk.Entry(root, width=30, show=show_char, font=("Arial", 11), bd=1, relief="solid")
    ent.grid(row=2 + i, column=1, columnspan=3, sticky="w", padx=5, pady=5)
    entries[label_txt] = ent

# --- 3. ПЕРЕКЛЮЧАТЕЛИ (Radiobutton): Ваш возраст ---
lbl_age = tk.Label(root, text="Ваш возраст", font=("Arial", 11), bg=BG_COLOR)
lbl_age.grid(row=5, column=0, sticky="w", padx=15, pady=10)

age_var = tk.StringVar(value="До 20")
ages = ["До 20", "20-30", "30-50", "Старше 50"]

age_frame = tk.Frame(root, bg=BG_COLOR)
age_frame.grid(row=5, column=1, columnspan=3, sticky="w", padx=5)

for age in ages:
    rb = ttk.Radiobutton(age_frame, text=age, value=age, variable=age_var)
    rb.pack(side="left", padx=5)

# --- 4. ФЛАЖКИ (Checkbutton): На каких языках читаете ---
lbl_lang = tk.Label(root, text="На каких языках читаете:", font=("Arial", 11), bg=BG_COLOR)
lbl_lang.grid(row=6, column=0, sticky="w", padx=15, pady=10)

languages = ["Русский", "Английский", "Французский", "Немецкий"]
lang_vars = {}

lang_frame = tk.Frame(root, bg=BG_COLOR)
lang_frame.grid(row=6, column=1, columnspan=3, sticky="w", padx=5)

for lang in languages:
    var = tk.BooleanVar(value=True if lang == "Русский" else False)
    lang_vars[lang] = var
    cb = ttk.Checkbutton(lang_frame, text=lang, variable=var)
    cb.pack(side="left", padx=5)

# --- 5. ВЫБОР ФОРМАТА (Listbox) ---
lbl_fmt = tk.Label(root, text="Какой формат данных является для вас предпочтительным?",
                   font=("Arial", 11), bg=BG_COLOR)
lbl_fmt.grid(row=7, column=0, columnspan=4, sticky="w", padx=15, pady=(10, 2))

listbox_fmt = tk.Listbox(root, height=2, width=15, font=("Arial", 11), bd=1, relief="solid")
listbox_fmt.insert(1, "HTML")
listbox_fmt.insert(2, "Plain text")
listbox_fmt.select_set(0)  # Выделяем HTML по умолчанию
listbox_fmt.grid(row=8, column=0, sticky="w", padx=15, pady=5)

# --- 6. ТЕКСТОВАЯ ОБЛАСТЬ: Любимые авторы ---
lbl_auth = tk.Label(root, text="Ваши любимые авторы:", font=("Arial", 11), bg=BG_COLOR)
lbl_auth.grid(row=9, column=0, columnspan=4, sticky="w", padx=15, pady=(10, 2))

text_authors = tk.Text(root, height=4, width=50, font=("Arial", 11), bd=1, relief="solid")
text_authors.grid(row=10, column=0, columnspan=4, sticky="w", padx=15, pady=5)

# --- 7. КНОПКИ (OK / Отменить) ---
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.grid(row=11, column=0, columnspan=4, sticky="w", padx=15, pady=10)

btn_ok = tk.Button(btn_frame, text="  OK  ", font=("Arial", 10), bd=1, relief="raised")
btn_ok.pack(side="left", padx=(0, 10))

btn_cancel = tk.Button(btn_frame, text="Отменить", font=("Arial", 10), bd=1, relief="raised")
btn_cancel.pack(side="left")

# --- 8. НИЖНИЙ ИНФОРМАЦИОННЫЙ БЛОК ---
lbl_php = tk.Label(root, text="Проверка PHP Лабораторные по базам данных",
                   font=("Arial", 11), bg=BG_COLOR)
lbl_php.grid(row=12, column=0, columnspan=4, sticky="w", padx=15, pady=(15, 5))

# Серая рамка "Лабораторные по базам данных"
frame_db = tk.Frame(root, bd=1, relief="solid", bg="#E0E0E0")
frame_db.grid(row=13, column=0, columnspan=4, sticky="we", padx=15, pady=5)
lbl_db = tk.Label(frame_db, text="Лабораторные по базам данных", font=("Arial", 10), bg="#E0E0E0")
lbl_db.pack(pady=3, fill="x")

# Финальный текст по центру
lbl_footer1 = tk.Label(root, text="Сегодня замечательный день.", font=("Arial", 11), bg=BG_COLOR)
lbl_footer1.grid(row=14, column=0, columnspan=4, pady=(10, 2))

lbl_footer2 = tk.Label(root, text="Я сделал свою первую интернет страничку.", font=("Arial", 11), bg=BG_COLOR)
lbl_footer2.grid(row=15, column=0, columnspan=4, pady=2)

lbl_footer3 = tk.Label(root, text="я буду богатым и свободным человеком !",
                       font=("Arial", 11, "italic"), fg="blue", bg=BG_COLOR)
lbl_footer3.grid(row=16, column=0, columnspan=4, pady=2)

# Запуск программы
root.mainloop()
