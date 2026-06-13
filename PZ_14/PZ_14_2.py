import tkinter as tk
from tkinter import messagebox


def calc():
    try:
        n = int(entry.get())
        if n <= 999:
            messagebox.showerror("Ошибка", "Число должно быть больше 999")
            return

        hundred = (n // 100) % 10
        result.config(text=f"Цифра сотен: {hundred}")
    except:
        messagebox.showerror("Ошибка", "Введите целое число")


root = tk.Tk()
root.geometry("300x100")
root.resizable(False, False)
root.title("Сотни")

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Посчитать", command=calc).pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()