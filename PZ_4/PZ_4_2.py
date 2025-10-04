# Найти максимальное целое K, что 1 + 1/2 + ... + 1/K < A, где A > 1.
# Вывести K и саму сумму.

try:
    a = float(input("Введите A (> 1): "))
except ValueError:
    print("Ошибка: A должно быть числом")
else:
    if a <= 1.0:
        print("Ошибка: A должно быть больше 1")
    else:
        k = 0
        harmonic_sum = 0.0

        # Увеличиваем k, пока сумма строго меньше A
        while True:
            next_k = k + 1
            next_sum = harmonic_sum + 1.0 / next_k
            if next_sum < a:
                k = next_k
                harmonic_sum = next_sum
            else:
                break

        print("Максимальное K:", k)
        print("Сумма 1 + 1/2 + ... + 1/K:", harmonic_sum)