



try:
    deposit = int(input("Введите сумму вклада в рублях: "))

    if deposit <= 0:
        print("Ошибка: сумма должна быть положительной")
    elif deposit <= 50000:
        print("Процентная ставка: 4%")
    elif deposit <= 100000:
        print("Процентная ставка: 5%")
    elif deposit <= 150000:
        print("Процентная ставка: 6%")
    elif deposit <= 200000:
        print("Процентная ставка: 7%")
    else:
        print("Для суммы свыше 200000 руб. процент не задан")
except ValueError:
    print("Ошибка: введено не число")