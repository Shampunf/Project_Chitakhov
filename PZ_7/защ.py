
mail = input("Введите почту:")

def maskEmail(mail):
    a = mail.find("@")
    prom = mail[a-1:]
    res = (mail[0:1] + ("*" * (a-1)) + prom)
    return res


print(maskEmail(mail))