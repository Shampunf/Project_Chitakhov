# Сумма: X - X**3/3 + X**5/5 - ... + (-1)**N * X**(2N+1)/(2N+1), при |X| < 1, N > 0

try:
    x = float(input("Введите вещественное X (|X| < 1): "))
except ValueError:
    print("Ошибка: X должно быть числом")
else:
    try:
        n = int(input("Введите целое N (> 0): "))
    except ValueError:
        print("Ошибка: N должно быть целым числом")
    else:
        if abs(x) >= 1:
            print("Ошибка: |X| должно быть строго меньше 1")
        elif n <= 0:
            print("Ошибка: N должно быть больше 0")
        else:
            k = 0
            series_sum = 0.0
            while k <= n:
                numerator = (-1) ** k * (x ** (2 * k + 1))
                denominator = 2 * k + 1
                series_sum += numerator / denominator
                k += 1

            print("Значение суммы (приближение arctg(x)):", series_sum)