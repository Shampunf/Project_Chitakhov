import sqlite3
import employers

conn = sqlite3.connect("buhgalteria.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Статья_Расходов (
    Код INTEGER PRIMARY KEY AUTOINCREMENT,
    Фамилия TEXT, Место_Командировки TEXT, Вид_расхода TEXT, Сумма_Расходов INTEGER)""")
cur.executemany("""INSERT INTO Статья_Расходов (Фамилия, Место_Командировки, Вид_расхода, Сумма_Расходов)
    VALUES (?, ?, ?, ?)""",  employers.EXPENSES)

def show():
    for row in cur.execute("SELECT * FROM Статья_Расходов").fetchall():
        print(row)

show()

name = input("\n Добавить запись:\n Фамилия")
place = input("\n Место командировки:")
tipe = input("\n Вид расходов: ")
summ = int(input("\n Сумма:"))
str = [name, place, tipe, summ]
cur.execute("""INSERT INTO Статья_Расходов (Фамилия, Место_Командировки, Вид_расхода, Сумма_Расходов)
    VALUES (?, ?, ?, ?)""", str )
show()