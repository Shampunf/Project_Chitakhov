import sqlite3
import workers

conn = sqlite3.connect("office.db")
cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS Канцелярия (
    Код INTEGER PRIMARY KEY AUTOINCREMENT,
    ФИО TEXT, Отдел TEXT, Вид_расхода TEXT, Сумма INTEGER)""")
cur.execute("DELETE FROM Канцелярия")
cur.execute("DELETE FROM sqlite_sequence WHERE name='Канцелярия'")
cur.executemany("""INSERT INTO Канцелярия (ФИО, Отдел, Вид_расхода, Сумма)
    VALUES (?, ?, ?, ?)""",  workers.EXPENSES)
conn.commit()

def show():
    for row in cur.execute("SELECT * FROM Канцелярия").fetchall():
        print(row)

def find():
    # 3 критерия поиска: ФИО, отдел, сумма
    print("1-ФИО  2-Отдел  3-Сумма")
    c, v = input("Критерий: "), input("Значение: ")
    try:
        queries = {
            "1": ("SELECT * FROM Канцелярия WHERE ФИО LIKE ?", (f"%{v}%",)),
            "2": ("SELECT * FROM Канцелярия WHERE Отдел = ?", (v,)),
            "3": ("SELECT * FROM Канцелярия WHERE Сумма = ?", (int(v),)),
        }
        if c not in queries:
            return print("Неверный критерий.")
        result = cur.execute(*queries[c]).fetchall()
        [print(r) for r in result] if result else print("Не найдено.")
    except ValueError:
        print("Ошибка: сумма должна быть числом.")

def delete():
    # 3 критерия удаления: код, ФИО, вид расхода
    print("1-Код  2-ФИО  3-Вид расхода")
    c, v = input("Критерий: "), input("Значение: ")
    try:
        queries = {
            "1": ("DELETE FROM Канцелярия WHERE Код = ?", (int(v),)),
            "2": ("DELETE FROM Канцелярия WHERE ФИО LIKE ?", (f"%{v}%",)),
            "3": ("DELETE FROM Канцелярия WHERE Вид_расхода = ?", (v,)),
        }
        if c not in queries:
            return print("Неверный критерий.")
        cur.execute(*queries[c])
        conn.commit()
        print(f"Удалено: {cur.rowcount}")
    except ValueError:
        print("Ошибка: код должен быть числом.")

def edit():
    # Находим запись по коду, затем меняем одно из трёх полей
    try:
        code = int(input("Код записи: "))
        rec = cur.execute(
            "SELECT * FROM Канцелярия WHERE Код = ?", (code,)
        ).fetchone()
        if not rec:
            return print("Не найдена.")
        print(rec)
        print("1-Отдел  2-Вид расхода  3-Сумма")
        fields = {"1": "Отдел", "2": "Вид_расхода", "3": "Сумма"}
        f = input("Что изменить: ")
        if f not in fields:
            return print("Неверный критерий.")
        cur.execute(
            f"UPDATE Канцелярия SET {fields[f]} = ? WHERE Код = ?",
            (input("Новое значение: "), code)
        )
        conn.commit()
        print("Обновлено.")
    except ValueError:
        print("Ошибка: код должен быть числом.")

while True:
    print("\n1-Показать  2-Найти  3-Удалить  4-Редактировать  0-Выход")
    choice = input("Выбор: ")
    if   choice == "1": show()
    elif choice == "2": find()
    elif choice == "3": delete()
    elif choice == "4": edit()
    elif choice == "0": break

conn.close()
