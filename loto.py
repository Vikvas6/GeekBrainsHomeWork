#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

class Card:
  
  def __init__(self, title):
    self.title = title
    self.generate()
    self.remaining = 15

  #Все числа запишем, как строки с 3мя символами
  @staticmethod
  def num_as_cell(number):
    if number < 10:
      result = '  ' + str(number) 
    else:
      result = ' ' + str(number)
    return result

  def _create_line(self, elements):
    elements.sort(reverse=True)
    line_prototype = ['   ' for i in range(4)]
    line_prototype += ['***' for i in range(5)]
    random.shuffle(line_prototype)
    result = ''
    for i in line_prototype:
      if i == '   ':
        result += '   '
      else:
        result += elements.pop()
    return result[1:]
        
  def generate(self):
    list_of_numbers = []
    first_line = []
    second_line = []
    third_line = []
    while len(list_of_numbers) < 15:
      new_number = self.num_as_cell(random.randint(1, 90))
      if new_number in list_of_numbers:
        continue
      list_of_numbers.append(new_number)
      if len(list_of_numbers) % 3 == 0:
        first_line.append(new_number)
      elif len(list_of_numbers) % 3 == 1:
        second_line.append(new_number)
      else:
        third_line.append(new_number)

    self.l0 = list_of_numbers
    self.l1_data = first_line.copy()   
    self.l2_data = second_line.copy() 
    self.l3_data = third_line.copy()      
    self.l1 = self._create_line(first_line)
    self.l2 = self._create_line(second_line)
    self.l3 = self._create_line(third_line)

  def __str__(self):
    result = self.title + '\n'
    result += self.l1 + '\n'
    result += self.l2 + '\n'
    result += self.l3 + '\n'
    result += '--------------------------'
    return result

  def is_number_on_card(self, number):
    return number in self.l0

  @staticmethod
  def _replace_in_line(line, number):
    if line.find(number) > -1:
      return line.replace(number, '  -')
    else:
      return line.replace(number[1:], ' -')

  def strike_out(self, number, silent=False):
    if self.is_number_on_card(number):
      self.remaining -= 1
      if number in self.l1_data:
        self.l1 = self._replace_in_line(self.l1, number)
      elif number in self.l2_data:
        self.l2 = self._replace_in_line(self.l2, number)
      else:
        self.l3 = self._replace_in_line(self.l3, number)
    elif not silent:
      print('У вас нет такого номера')
    if self.remaining > 0:
      return False
    return True


class Loto:
  user_title = '------ Ваша карточка -----'
  comp_title = '-- Карточка компьютера ---'
  prev_values = []

  def _get_next(self):
    while len(self.prev_values) < 90:
      next_num = Card.num_as_cell(random.randint(1,90))
      if next_num in self.prev_values:
        continue
      self.prev_values.append(next_num)
      yield next_num

  def start_game(self):
    self.prev_values = []
    user_card = Card(self.user_title)
    comp_card = Card(self.comp_title)
    remaining = 90

    while remaining > 0:
      current_gen = self._get_next()
      current = current_gen.__next__()
      remaining -= 1
      print('Новый бочонок: {} (осталось {})'.format(current, remaining))
      print(user_card)
      print(comp_card)
      print('Зачеркнуть цифру? (y/n)')
      resp = input()
      if resp == 'y' or resp == 'Y':
        if user_card.strike_out(current):
          print('Вы победили! Еще раз? (y/n)')
          resp = input()
          if resp == 'y' or resp == 'Y':
            self.start_game()
          else:
            break
      if comp_card.strike_out(current, silent=True):
        print('Увы, машина победила человека... Еще раз? (y/n)')
        resp = input()
        if resp == 'y' or resp == 'Y':
          self.start_game()
        else:
          break

game = Loto()
game.start_game()

