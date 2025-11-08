# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить
# функцией с параметрами. Значения n и m программа должна запрашивать.
def funcSum(num1,num2):
    if(num1>num2):
        print("num1 is greater than num2")
        return 0
    i = num1
    numer = 0
    while i < num2:
        numer += i  # складываем пока не дойдем до второго числа
        i += 1
    else:
        return numer

try:
    n = int(input("Введите целое число ")) # ввод данных
    m = int(input("Введите целое число "))
except ValueError:
    print("Введите натуральное число ") # валидация и обработка ошибок
else:
    num = funcSum(n,m)
    print(num)
