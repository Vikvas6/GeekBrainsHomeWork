import re

#Класс доски для игры, содержит в себе размеры и текущую позицию
class Board:

    #Для простоты будем играть на квадратном поле
    def __init__(self, length):
        self.len = length
        self.turn_pattern = r'^\d?\d \d?\d$'
        self.board = ('-'*self.len+'\n')*self.len
        self.winning_line = 5
    
    #Сделать ход в указанную точку указанным символом, если туда можно походить - вернём True, если нет - напишем сообщение и вернём False
    def make_turn(self, turn, point):
        if re.match(self.turn_pattern, turn):
            a,b = turn.split(' ')
            a = int(a)
            b = int(b)
            tmp = list(self.board)
            if tmp[(a-1)*(self.len+1) + (b-1)] != '-':
                print("Сюда ходить нельзя!")
                return False
            tmp[(a-1)*(self.len+1) + (b-1)] = point
            self.board = "".join(tmp)
            return True
        else:
            return False

    #Вывести на экран поле с легендой
    def __str__(self):
        result = '   '
        for i in range(self.len):
            if i < 9:
                result += '  ' + str(i+1)
            else:
                result += ' ' + str(i+1)
        result += '\n'
        for i in range(self.len):
            if i < 9:
                result += '  ' + str(i+1)
            else:
                result += ' ' + str(i+1)
            for j in range(self.len):
                result += '  ' + self.board[i*(self.len+1)+j]
            result += '\n'

        return result

    #Проверка на победу, и вывод на экран финальной позиции
    def is_win(self, char):
        if self._get_max_line(char) == self.winning_line:
            print(self)
            return True
        return False
                
    #Вернуть символ на позиции a,b (счет от 0)
    def _get_char_at(self, a, b):
        return self.board[a*(self.len+1) + b]

    #Для проверки на победу - получить самую длинную линию выбранного символа
    def _get_max_line(self, char):
        resultlen = 0
        curlen = 0
        for i in range(self.len):
            for j in range(self.len):
                if self._get_char_at(i, j) == char:
                    curlen = self._get_line(i, j, char, 0, 1)
                    if curlen > resultlen:
                        resultlen = curlen
                    curlen = self._get_line(i, j, char, 1, 0)
                    if curlen > resultlen:
                        resultlen = curlen
                    curlen = self._get_line(i, j, char, 1, 1)
                    if curlen > resultlen:
                        resultlen = curlen
                    curlen = self._get_line(i, j, char, 1, -1)
                    if curlen > resultlen:
                        resultlen = curlen
        return resultlen                    
    
    #Получить длину линии выбранного символа в указанном направлении, mod_ - указание направления (0 - не двигаемся (для вертикальных и горизонтальных линий))
    def _get_line(self, a, b, char, mod_a, mod_b):
        resultlen = 0
        for i in range(self.winning_line):
            if (a + i*mod_a) < self.len and (a + i*mod_a) > -1 and (b + i*mod_b) < self.len and (b + i*mod_b) > -1 \
            and self._get_char_at(a + i*mod_a, b + i*mod_b) == char:
                resultlen += 1
            else:
                break
        return resultlen

#Класс самой игры
class Game:

    #Начало игры, т.к. самой игры нет - этот метод статический
    @staticmethod
    def start_game():
        print("Вы хотите начать игру? (Д/н)")
        answer = input()
        if answer == 'y' or answer == 'Y' or answer == 'д' or answer == 'Д' or answer == '':
            print("""Выберите режим игры:
Режим    х       о
  1   Человек Человек
  2   Человек    ИИ
  3      ИИ   Человек
  4      ИИ      ИИ""")
            answer = input()
            if answer == '1':
                game = Game(HumanPlayer('Игрок 1'), HumanPlayer('Игрок 2'))
            elif answer == '2':
                game = Game(HumanPlayer('Игрок'), AIPlayer('ИИ'))
            elif answer == '3':
                game = Game(AIPlayer('ИИ'), HumanPlayer('Игрок'))
            elif answer == '4':
                game = Game(AIPlayer('ИИ 1'), AIPlayer('ИИ 2'))
            game._game_begin()

    #Печать правил (вызывается перед каждой играть)
    @staticmethod
    def print_rules():
        print("Ход задаётся 2мя координатами через пробел от 1 до длины поля, первое число по вертикали, второе - по горизонтали")
        print("Если Вы хотите закончить игру - введите exit")

    #Создаём игру с 2мя игроками и печатаем правила
    def __init__(self, player1, player2):
        Game.print_rules()
        self.player1 = player1
        self.player2 = player2

    #Начинаем игру - создаём поле, просим ввести меньеш 100, чтобы не париться с легендой (да и не играют на слишком больших полях)
    def _game_begin(self):
        print("Введите желаемую длину поля (меньше 100):")
        length = int(input())
        self.board = Board(length)
        self._play()
        self.start_game()

    #Сделать ход игроком player1, вызывается метод из класса игрока чтобы на выходе получить строку 'a b' в качестве хода
    #Если ход невозможный - проявим характер и накажем игрока
    def _make_turn(self, player1, player2, char):
        turn = player1.make_turn(self.board, char)
        if turn:
            if not self.board.make_turn(turn, char):
                print(player1.name + ' сделал невозможный с точки зрения правил ход.')
                print('Это расценивается как прямое оскорбление спортивного духа и поэтому ' + player1.name + ' наказан проигрышем!')
                print(player2.name + ' победил!')
                return False
            if self.board.is_win(char):
                print(player1.name + ' победил!')
                return False
        else:
            print(player1.name + ' прервал игру.')
            return False
        return True

    #Один раунд игры
    def _play(self):
        while True:
            if not self._make_turn(self.player1, self.player2, 'x'):
                break
            if not self._make_turn(self.player2, self.player1, 'o'):
                break

#Абстрактный класс игрока
class Player:
    def make_turn(self, board, char):
        pass

    def __init__(self, name):
        self.name = name

#Класс игрока-человека, сделать ход = спросить у пользователя
class HumanPlayer(Player):
    def make_turn(self, board, char):
        print(board)
        print(self.name + ", введите Ваш ход (exit чтобы закончить):")
        turn = input()
        if turn == 'exit':
            return False
        else:
            return turn

#Класс игрока-компьютера, сделать ход = с помощью хитрого (но тупого) алгоритма выбрать лучшую позицию
class AIPlayer(Player):

    #Попробуем найти лучший ход присваивая веса каждой клеточке
    def make_turn(self, board, char):
        print(board)
        list_turns = []
        for i in range(board.len):
            for j in range(board.len):
                list_turns.append((i, j, self._get_weight(board, i, j, char, 'x' if char == 'o' else 'o')))
        
        best_turn = (-1, -1, 0)
        for i in list_turns:
            if i[2] > best_turn[2]:
                best_turn = i
        return str(best_turn[0]+1) + ' ' + str(best_turn[1]+1)

    #Посмотрим во все направления и сопоставим каждому направлению какой-то вес, итоговый вест будет суммой этих весов
    def _get_weight(self, board, a, b, char, char2):
        if board._get_char_at(a, b) != '-':
            return 0
        else:
            return self._wl(board, a, b, char, char2, 0, 1) \
                 + self._wl(board, a, b, char, char2, 0, -1) \
                 + self._wl(board, a, b, char, char2, 1, 0) \
                 + self._wl(board, a, b, char, char2, 1, 1) \
                 + self._wl(board, a, b, char, char2, 1, -1) \
                 + self._wl(board, a, b, char, char2, -1, 0) \
                 + self._wl(board, a, b, char, char2, -1, 1) \
                 + self._wl(board, a, b, char, char2, -1, -1) 

    #Вес одного направления - смотрим, сколько собирается в ряд и на основании этого высчитываем вес
    def _wl(self, board, a, b, char, char2, mod_a, mod_b):
        result = 0.1
        last_char = ''
        for i in range(1, 3):
            if a+i*mod_a >= board.len or a+i*mod_a < 0 or b+i*mod_b >= board.len or b+i*mod_b < 0:
                result = result/2
                break
            if board._get_char_at(a+i*mod_a, b+i*mod_b) == '-':
                result += 0.1/i
                last_char = '-'
            elif board._get_char_at(a+i*mod_a, b+i*mod_b) == char:
                if last_char == char or last_char == '':
                    result += 0.2*i**2
                    if i == 3:
                        result += 100
                else:
                    break
                last_char = char
            elif board._get_char_at(a+i*mod_a, b+i*mod_b) == char2:
                if last_char == char2 or last_char == '':
                    result += 0.1*i**2
                    if i == 3:
                        result += 50
                else:
                    break
                last_char = char2
        return result



Game.start_game()