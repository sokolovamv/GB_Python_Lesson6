# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

import random

n = int(input("Введите число: "))
position = list(map(int, input("Введите через пробел 2 позиции: ").split()))
print(len(position) != 2 and - 1 > position[0] >= n and - 1 > position[1] >= n)
while len(position) != 2 or not (0 <= position[0] <= n) or not (0 <= position[1] <= n):
    position = list(map(int, input("Введите через пробел 2 позиции: ").split()))
number_list = [random.randint(-n, n) for _ in range(n)]
print(number_list)
result = lambda x, y: x * y
print(result(number_list[position[0]], number_list[position[1]]))
