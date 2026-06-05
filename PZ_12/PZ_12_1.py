"""В матрице найти минимальный элемент в предпоследнем столбце."""

from random import randint

# Создаем матрицу 4 на 5 с помощью спискового включения
matrix = [[randint(-10, 10) for j in range(5)] for i in range(4)]

# Выводим исходную матрицу
print("Исходная матрица:")
for row in matrix:
    print(row)

# Находим предпоследнюю строку
preLastRow = matrix[-2]

# Находим минимальный элемент в предпоследней строке
min_element = min(preLastRow)
# Выводим результат
print("\nПредпоследняя строка:")
print(preLastRow)

print("Минимальный элемент в предпоследней строке:", min_element)