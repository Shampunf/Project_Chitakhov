"""Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
переопределите методы, связанные с вычислением площади и периметра."""
class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Rectangle(Figure):
    pass


class Square(Figure):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width ** 2

    def perimeter(self):
        return self.weight*4
r=Regtangle()
r.weight = 10
r.height = 20
print(r.area())


s=Square()
s.weight = 10
s.height = 10
print(s.area(),s.perimeter())
