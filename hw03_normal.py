# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

#'''
def fibonacci(n, m):
    i = 1
    num_last = 0
    num = 1
    while i <= m:
        if i >= n:
            print(num)
        if i >= m:
            break
        num = num + num_last
        num_last = num - num_last
        i += 1
#1 2 3 4 5 6  7  8  9
#1 1 2 3 5 8 13 21 34
print("Введите номера граничных элементов (включительно): ")
n = int(input())
m = int(input())
fibonacci(n, m)
#'''

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

#'''
def sort_to_max(origin_list):
    for j in range(len(origin_list)-1):
        for i in range(len(origin_list) - j - 1):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i+1] = origin_list[i+1] + origin_list[i]
                origin_list[i] = origin_list[i+1] - origin_list[i]
                origin_list[i+1] = origin_list[i+1] - origin_list[i]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
#'''

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

#'''
def my_own_filter(flt_func, array):
    new_array = []
    for i in array:
        if flt_func(i):
            new_array.append(i)
    return new_array

print(my_own_filter(lambda x: x<0, range(-5, 5)))
#'''

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parblablagramm(a1, a2, a3, a4):
    #У параллелограмма стороны попарно равны, тогда и квадраты сторон попарно равны, найдём эти квадраты сторон
    #Из-за расположения точек может так получиться, что мы найдём 2 стороны и 2 диагонали, но если он попарно равны - это тоже параллелограмм (надеюсь)
    a1a2 = (a2[0] - a1[0]) ** 2 + (a2[1] - a1[1]) ** 2
    a2a3 = (a3[0] - a2[0]) ** 2 + (a3[1] - a2[1]) ** 2
    a3a4 = (a4[0] - a3[0]) ** 2 + (a4[1] - a3[1]) ** 2
    a4a1 = (a1[0] - a4[0]) ** 2 + (a1[1] - a4[1]) ** 2
    
    if a1a2 == a3a4 and a2a3 == a4a1:
        return True
    return False

print(is_parblablagramm((0,0), (0,3), (2,0), (2,3)))