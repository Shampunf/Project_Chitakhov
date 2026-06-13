"""В матрице найти минимальный элемент в предпоследнем столбце."""

from random import randint

matrix = [[randint(-10, 10) for j in range(5)] for i in range(4)]

print("Исходная матрица:")
for row in matrix:
    print(row)

preLastRow = matrix[-2]

minElement = min(preLastRow)
# Выводим результат
print("\nПредпоследняя строка:")
print(preLastRow)

print("Минимальный элемент в предпоследней строке:", minElement)