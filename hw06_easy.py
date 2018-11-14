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
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    #Расстояние между 2мя точками, чтобы найти длину сторон треугольника
    def _get_delta(self, p1, p2):
        return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    #Найти коэффициент наклона отрезка
    def _get_k(self, p1, p2):
        if p2[0] == p1[0]:
            if p2[1] > p1[1]:
                return float('+inf')
            elif p2[1] < p1[1]:
                return float('-inf')
            else:
                return float('nan')
        return (p2[1] - p1[1])/(p2[0] - p1[0])

    #Найти диагонали фигуры
    def _get_diag(self):
        kdAB = self._get_k(self.A, self.B)
        kdAC = self._get_k(self.A, self.C)
        kdAD = self._get_k(self.A, self.D)
        if (kdAB - kdAC)*(kdAD - kdAC) < 0:
            return [(self.A, self.C), (self.B, self.D)]
        elif (kdAC - kdAB)*(kdAD - kdAB) < 0:
            return [(self.A, self.B), (self.C, self.D)]
        elif (kdAB - kdAD)*(kdAC - kdAD) < 0:
            return [(self.A, self.D), (self.B, self.C)]
        else:
            return []

    #Проверка на параллельность
    def _is_parallel(self, AB, CD):
        return self._get_k(AB[0], AB[1]) == self._get_k(CD[0], CD[1]) or self._get_k(AB[0], AB[1]) == - self._get_k(CD[0], CD[1])

    #Проверка, является ли фигура равнобочной трапецией
    def is_ravn_trap(self):
        return (self._is_parallel((self.A, self.B), (self.C, self.D)) and self._get_delta(self.A, self.B) == self._get_delta(self.C, self.D)) \
            or (self._is_parallel((self.A, self.C), (self.B, self.D)) and self._get_delta(self.A, self.C) == self._get_delta(self.B, self.D)) \
            or (self._is_parallel((self.A, self.D), (self.B, self.C)) and self._get_delta(self.A, self.D) == self._get_delta(self.B, self.C))

    #Сумма длин сторон
    def perimeter(self):
        return self._get_delta(self.A, self.B) + self._get_delta(self.B, self.C) + self._get_delta(self.C, self.D) + self._get_delta(self.D, self.A)

    #Разобьём фигуру на 2 треугольника (по диагонали) и посчитаем суммарную площадь
    def square(self):
        diags = self._get_diag()
        if len(diags) > 1:
            triangle_1 = Triangle(diags[0][0], diags[0][1], diags[1][0])
            triangle_2 = Triangle(diags[0][0], diags[0][1], diags[1][1])
            return triangle_1.square() + triangle_2.square()

    #Рёбра фигуры можно найти через диагонали
    def get_edges(self):
        edges = []        
        diags = self._get_diag()
        edges.append(self._get_delta(diags[0][0], diags[1][0]))
        edges.append(self._get_delta(diags[0][0], diags[1][1]))
        edges.append(self._get_delta(diags[0][1], diags[1][0]))
        edges.append(self._get_delta(diags[0][1], diags[1][1]))
        return edges

b = Trapets((0,0), (1,1), (3,1), (4,0))
print(b.is_ravn_trap()) #True
print(b.square())       #3
print(b.perimeter())    #6 + 2*sqrt(2)
print(b.get_edges())    #sqrt(2), 2, sqrt(2), 4