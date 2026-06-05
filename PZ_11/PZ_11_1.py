"""Даны текущие оценки студента по дисциплине «Основы программирования» за месяц.
 Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и определить итоговую оценку за месяц."""

from random import randint

marks = [randint(2, 5) for i in range(10)]

print("Оценки:", marks)

print("Количество 2:", marks.count(2))
print("Количество 3:", marks.count(3))
print("Количество 4:", marks.count(4))
print("Количество 5:", marks.count(5))

final_mark = round(sum(marks) / len(marks))

print("Итоговая оценка:", final_mark)