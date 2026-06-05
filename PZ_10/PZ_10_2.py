"""Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое, количество букв в верхнем регистре.
Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы третей строки их числовыми кодами."""

f = open("text18-22.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

text = "".join(lines)

print("Содержимое файла:")
print(text)

count_upper = 0

for symbol in text:
    if symbol.isupper():
        count_upper += 1

print("Количество букв в верхнем регистре:", count_upper)

# заменяем символы третьей строки их числовыми кодами
lines[2] = " ".join(str(ord(symbol)) for symbol in lines[2]) + "\n"

new_file = open("result.txt", "w", encoding="utf-8")
new_file.writelines(lines)
new_file.close()
