import re

with open("ip_address.txt", "r", encoding="utf-8") as file:
    text = file.read()

section = re.search(
    r"Частоупотребимые маски(.*?)Количество адресов",
    text,
    re.DOTALL).group(1)

pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

masks = re.findall(pattern, section)

zero_fourth = [mask for mask in masks if mask.split(".")[3] == "0"]

other_masks = [mask for mask in masks if mask.split(".")[3] != "0"]

with open("zero_fourth.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(zero_fourth))

with open("other_masks.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(other_masks))

print("Маски с нулевым четвертым октетом:")
print(zero_fourth)
print("Количество строк:", len(zero_fourth))

print("\nОстальные маски:")
print(other_masks)
print("Количество строк:", len(other_masks))

