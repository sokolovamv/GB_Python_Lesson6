# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

coords_1 = list(map(int, input("Введите координаты точки 1: ").split()))
coords_2 = list(map(int, input("Введите координаты точки 2: ").split()))
distance = lambda x, y: ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1/2)
print(round(distance(coords_1, coords_2),3))