from random import randint

a = [randint(-20, 20) for i in range(10)]
b = [randint(-20, 20) for j in range(10)]

f1 = open("file1.txt", "w", encoding="utf-8")
f1.write(str(a))
f1.close()

f2 = open("file2.txt", "w", encoding="utf-8")
f2.write(str(b))
f2.close()

even = [x for x in a if x % 2 == 0]
odd = [x for x in b if x % 2 != 0]
positive_sum = sum([x for x in b if x > 0])

result = open("result.txt", "w", encoding="utf-8")

result.write("Содержимое первого файла: ")
result.write(str(a) + "\n")
result.write("Четные элементы: ")
result.write(str(even) + "\n")
result.write("Количество четных элементов: ")
result.write(str(len(even)) + "\n")
result.write("Среднее арифметическое: ")
result.write(str(sum(even) / len(even)) + "\n\n")

result.write("Содержимое второго файла: ")
result.write(str(b) + "\n")
result.write("Нечетные элементы: ")
result.write(str(odd) + "\n")
result.write("Количество нечетных элементов: ")
result.write(str(len(odd)) + "\n")
result.write("Сумма положительных элементов: ")
result.write(str(positive_sum))

result.close()

print("Готово")