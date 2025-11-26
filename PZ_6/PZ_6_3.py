"""Дано множество A из N точек на плоскости и точка B (точки заданы своими
координатами х, у). Найти точку из множества A, наиболее близкую к точке B.
Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по
формуле:
R = √(x2 – x1)2 + (у2 – y1)2
.
Для хранения данных о каждом наборе точек следует использовать по два списка: первый
список для хранения абсцисс, второй — для хранения ординат."""

import math
import random
N = int(input("Введите количество точек N: "))

xs = []
ys = []

print("координаты точек множества A (x y):")
for i in range(N):
    x, y = [random.randint(-10, 10) for i in range(2)]
    print(x,y)
    xs.append(x)
    ys.append(y)
bx = random.randint(-10, 10)
by = random.randint(-10, 10)
print("точка b: ",bx, by)

distance_Sq = None
index = -1

for i in range(N):
    dx = xs[i] - bx
    dy = ys[i] - by
    dist2 = dx * dx + dy * dy

    if distance_Sq is None or dist2 < distance_Sq:
        distance_Sq = dist2
        index = i

closest_x = xs[index]
closest_y = ys[index]
distance = math.sqrt(distance_Sq)

print("Ближайшая точка к B: (", closest_x, ",", closest_y, ")")
print("Расстояние до неё:", distance)

