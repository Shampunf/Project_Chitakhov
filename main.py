def main():
    """Выводит цифру в разряде сотен числа > 999 (через try/except)."""
    try:
        number = int(input("Введите число (> 999): "))
        if number <= 999:
            print("Ошибка: число должно быть больше 999")
            return

        hundreds_digit = (number // 100) % 10
        print("Цифра в разряде сотен:", hundreds_digit)

    except ValueError:
        print("Ошибка: введено не число")


if __name__ == "__main__":
    main()