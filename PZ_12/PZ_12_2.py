"""Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
элементов."""
from random import randint

matrix = [[randint(-10, 10) for _ in range(4)] for _ in range(5)]

print("Исходная матрица:")
list(map(print, matrix))

odd_rows = filter(lambda row: row[0] % 2 != 0,enumerate(matrix, start=1))

averages = map(lambda row: (row[0], sum(row[1]) / len(row[1])),odd_rows)

print("Среднее арифметическое строк с нечетным номером:")
list(map(lambda x: print(f"Строка {x[0]}: {x[1]}"), averages))