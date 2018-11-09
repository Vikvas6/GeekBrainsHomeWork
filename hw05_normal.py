# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy
import os
while True:
    print("Введите действие 1-4 (5 равносильно отмене)")
    i = input()
    if i == '1':
        print('Введите имя папки для перехода')
        try:
            os.chdir(input())
            print('Перешёл')
        except Exception:
            print('Невозможно перейти')
    if i == '2':
        hw05_easy.lis_dir()
    if i == '3':
        print('Введите имя папки для удаления')
        hw05_easy.delete_dir(input())
    if i == '4':
        print('Введите имя папки')
        hw05_easy.create_dir(input())
    if i == '5':
        break