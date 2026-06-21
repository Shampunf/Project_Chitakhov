
def cubeDigits(num):
    num = str(num)
    res = map(lambda d: str(int(d) ** 3),str(num))
    result =  "".join(res)
    return result

i = int(input("Введите число:  "))
print("\n", cubeDigits(i))

