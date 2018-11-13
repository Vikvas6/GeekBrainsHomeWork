# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    #Расстояние между 2мя точками, чтобы найти длину сторон треугольника
    def _get_delta(self, p1, p2):
        return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    #Сумма длин сторон
    def perimeter(self):
        return self._get_delta(self.A, self.B) + self._get_delta(self.B, self.C) + self._get_delta(self.C, self.A)

    #Используем формулу площади через полупериметр
    def square(self):
        perimeter_half = self.perimeter()/2
        return sqrt(perimeter_half * (perimeter_half - self._get_delta(self.A, self.B)) * (perimeter_half - self._get_delta(self.B, self.C)) * (perimeter_half - self._get_delta(self.C, self.A)) )

    #Площадь нашли через полупериметр, значит высоты можно найти по формуле площади через сторону и высоту 
    def get_heights(self):
        heights = []
        heights.append(2*self.square()/self._get_delta(self.A, self.B))
        heights.append(2*self.square()/self._get_delta(self.B, self.C))
        heights.append(2*self.square()/self._get_delta(self.C, self.A))
        return heights

a = Triangle((0,0), (0,2), (1,1))
print(a.perimeter())    #= 2 + sqrt(2)
print(a.square())       #= 1
print(a.get_heights())  #= 1, sqrt(2), sqrt(2)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapets:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    #Расстояние между 2мя точками, чтобы найти длину сторон треугольника
    def _get_delta(self, p1, p2):
        return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    #Сумма длин сторон
    def perimeter(self):
        return self._get_delta(self.A, self.B) + self._get_delta(self.B, self.C) + self._get_delta(self.C, self.A)

    #Используем формулу площади через полупериметр
    def square(self):
        perimeter_half = self.perimeter()/2
        return sqrt(perimeter_half * (perimeter_half - self._get_delta(self.A, self.B)) * (perimeter_half - self._get_delta(self.B, self.C)) * (perimeter_half - self._get_delta(self.C, self.A)) )

    #Площадь нашли через полупериметр, значит высоты можно найти по формуле площади через сторону и высоту 
    def get_heights(self):
        heights = []
        heights.append(2*self.square()/self._get_delta(self.A, self.B))
        heights.append(2*self.square()/self._get_delta(self.B, self.C))
        heights.append(2*self.square()/self._get_delta(self.C, self.A))
        return heights
