"""Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string.
 Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"""

import string

s = r'--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'
punctuation = ""
for symbol in s:
    if symbol in string.punctuation:
        punctuation += symbol

print(punctuation)