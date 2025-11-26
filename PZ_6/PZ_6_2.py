"""Даны списки A и B одинакового размера N. Поменять местами их содержимое и
вывести вначале элементы преобразованного списка A, а затем — элементы
преобразованного списка B."""

import random
N = int(input("Введите размер списков (N): "))
A = [random.randint(-5, 5) for i in range(N)]
B = [random.randint(-5, 5) for j in range(N)]
print("исходный cписок А:", A)
print("исходный cписок B:", B)
for i in range(N):
    A[i], B[i] = B[i], A[i]
print("cписок А:", A)
print("cписок B:", B)