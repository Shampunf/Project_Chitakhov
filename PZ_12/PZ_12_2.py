"""Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
элементов."""
from random import randint

matrix = [[randint(-10, 10) for j in range(4)] for i in range(5)]

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nСреднее арифметическое строк с нечетным номером:")

for i in range(len(matrix)):
    if (i + 1) % 2 != 0:
        average = sum(matrix[i]) / len(matrix[i])
        print(f"Строка {i + 1}: {average}")