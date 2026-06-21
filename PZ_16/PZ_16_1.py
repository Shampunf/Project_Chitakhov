""" Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
метод, который выводит информацию о товаре в формате "Название: название,
Цена: цена, Количество: кол-во"""
class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def info(self):
        print(f"Название: {self.name}, Цена: {self.price}, Количество: {self.count}")


a = Product("Яблоко", 50, 10)
a.info()
