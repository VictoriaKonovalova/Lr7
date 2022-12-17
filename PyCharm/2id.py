#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1. количество элементов списка, равных 0;
# 2. сумму элементов списка, расположенных после минимального элемента.
# Упорядочить элементы списка по возрастанию модулей элементов.


if __name__ == '__main__':
    a = list(map(int, input().split()))
    count = 0
    a_min = a[0]
    i_min = 0
    for index, value in enumerate(a):
        if value == 0:
            count += 1
        if value < a_min:
            i_min, a_min = index, value
    summ = sum(value for value in a[i_min + 1:])
    a.sort()
    print(a)
    print(f"Сумма = {summ}\nКол-во = {count}")
