# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

#'''
#Вряд ли это простейшее решение...
#Достаём из строки отдельные операнды и парсим их в кортеж бе целой части
def operand_parse(eq):
    a = 0
    b = 0
    c = 1
    if eq[-1] == ' ':
        eq = eq[:-1]
    if eq[0] == ' ':
        eq = eq[1:]

    if ' ' in eq:
        a = int(eq[:eq.find(' ')])
        if '/' in eq:
            b = int(eq[eq.find(' ')+1:eq.find('/')])
            c = int(eq[eq.find('/')+1:])
    else:
        if '/' in eq:
            b = int(eq[:eq.find('/')])
            c = int(eq[eq.find('/')+1:])
        else:
            a = int(eq)
    return (a*c+b, c)
    
print('Введите выражение')
eq = input()
list_of_oper = []
cur_oper = ''

#Формируем список, где по порядку расположены операнды и действия между ними
for i in eq:
    if i == '-' or i == '+':
        if cur_oper == '' or cur_oper == ' ':
            cur_oper += i
        else:
            list_of_oper.append(operand_parse(cur_oper))
            list_of_oper.append(i)
            cur_oper = ''
    else:
        cur_oper += i
list_of_oper.append(operand_parse(cur_oper))

#Считать будем попарно
def get_sum_of_two(oper1, sign, oper2):
    a1 = oper1[0] * oper2[1]
    a2 = oper2[0] * oper1[1]
    b = oper1[1] * oper2[1]
    if sign == '+':
        a = a1+a2
    else:
        a = a1 - a2
    return a, b

#После вычисления значения записываеся в левый операнд и происходит переход с следующему действию и операнду из списка
oper1 = ''
sign = ''
for i in list_of_oper:
    if oper1 == '':
        oper1 = i
    elif sign == '':
        sign = i
    else:
        oper1 = get_sum_of_two(oper1, sign, i)
        sign = ''

#Упрощение, начинаем проверять начиная с половинного значения, делится ли и числитель, и знаменатель на это число, если делится - сокращаем и запускаем рекурсивно
#если нет - уменьшаем число и проверяем снова, пока число не дойдёт до единицы (любое число делится на 1)
import math
def uprostit(oper1):
    s = abs(oper1[1] // 2)
    while s > 1:
        if oper1[0] % s == 0 and oper1[1] % s == 0:
            return uprostit((int(oper1[0]/s), int(oper1[1]/s)))
        else:
            s -= 1
    return oper1

a,b = uprostit(oper1)

#Выводим результат с выделением целой части
print('{} {}/{}'.format(a//b, a%b, b))
#'''

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

#'''
#функция пригодится для легкого парса таблиц в файле, без прибегания к импорту каких-либо библиотек
#превращает большое количество пробелов в один пробел, чтобы потом по этому пробелу разбить строку на колонки
def replace_spaces(ln):
    return ln.replace('     ', ' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ').replace('\n', '')

#сделаем последовательно - сначала просто кажду строку представим списком и соберем список таких списоков
list_workers = []
with open('data/workers', 'r', encoding='utf-8') as workers:
    workers.readline()
    for line in workers:
        list_workers.append(replace_spaces(line).split(' '))

#тоже самое со второй табличкой
list_hours = []
with open('data/hours_of', 'r', encoding='utf-8') as hours:
    hours.readline()
    for line in hours:
        list_hours.append(replace_spaces(line).split(' '))

#сделаем словарь для удобного обращения, где ключ - имя+фамилия, а значение - остальные столбцы таблицы в списке
dict_workers = {}
for i in list_workers:
    dict_workers[i[0] + '+' + i[1]] = i[2:]

#посчитаем запрплату
for i in list_hours:
    idx = i[0] + '+' + i[1]

    oklad = float(dict_workers[idx][0])
    norma = float(dict_workers[idx][2])
    real = float(i[2])
    hour_price = oklad / norma
    if norma > real:
        print(idx.replace('+', ' '), oklad + hour_price*(real - norma))
    else:
        print(idx.replace('+', ' '), oklad + 2*hour_price*(real - norma))
#'''


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

#'''
path = 'data/'

with open(path+'fruits.txt', 'r', encoding='utf-8') as f:
    for l in f:
        #знак перевода каретки будет, так что выбираем строки длиннее одного символа
        if len(l) > 1 or l != '\n':
            first_letter = l[0]
            filename = 'fruits_' + first_letter
            with open(path+filename, 'a', encoding='utf-8') as ff:
                ff.write(l)
#'''