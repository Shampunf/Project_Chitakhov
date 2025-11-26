"""Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
арифметическое всех элементов списка, кроме элементов с номерами от K до L
включительно."""
import random
k = int(input("Введите число K (1 < K ≤ L ≤ N): "))
l = int(input("Введите число L (1 < K ≤ L ≤ N): "))
N = int(input("Введите число N (1 < K ≤ L ≤ N): "))

count = N - l + k -1

lst = [random.randint(-5, 5) for i in range(N)]
print("исходный список: ", lst)
if(k > l or l > N or k < 1):
    print("(1 < K ≤ L ≤ N)")
else:
    summa = sum(lst)
    sum2 = sum(lst[k-1:l])
    print(count,  sum2)
    print("среднее африфметическое: ",(summa - sum2)/count)
