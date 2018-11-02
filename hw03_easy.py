# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    #Временное число, в котором все нужные нам цифры переносятся в целую часть
    temp_number = number * 10**ndigits
    #int() отбросит дробную часть => можем проверить величину дробной части
    if temp_number - int(temp_number) >= 0.5:
        temp_number += 1
    return int(temp_number)/10**ndigits



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    #Если в номере только одна цифра, номер по определению считается счастливым
    ticket_len = len(str(ticket_number))
    if ticket_len == 1:
        return True
    else:
        #Посчитаем сумму левых цифр и правых, если число цифр нечётное, то средняя цифра нас не интересует, поэтому делим число цифр нацело
        sum_left = 0
        sum_right = 0
        for i in range(ticket_len//2):
            sum_left += int(str(ticket_number)[i])
            sum_right += int(str(ticket_number)[-i-1])
        if sum_left == sum_right:
            return True
        return False



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(437751))
print(lucky_ticket(43651))
