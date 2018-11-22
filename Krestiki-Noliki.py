import re

class Board:

    def __init__(self, length):
        self._len = length
        self.turn_pattern = r'^\d?\d \d?\d$'
        self.board = ('-'*self._len+'\n')*self._len
        self.winning_line = 5
    
    def make_turn(self, turn, point):
        if re.match(self.turn_pattern, turn):
            a,b = turn.split(' ')
            a = int(a)
            b = int(b)
            tmp = list(self.board)
            if tmp[(a-1)*(self._len+1) + (b-1)] != '-':
                print("Сюда ходить нельзя!")
                return False
            tmp[(a-1)*(self._len+1) + (b-1)] = point
            self.board = "".join(tmp)
            return True
        else:
            return False

    def __str__(self):
        return self.board

    def is_win(self, char):
        if self._get_max_line(char) == self.winning_line:
            print(self)
            return True
        return False
                
    #Вернуть символ на позиции a,b (счет от 0)
    def _get_char_at(self, a, b):
        return self.board[a*(self._len+1) + b]

    def _get_max_line(self, char):
        result_len = 0
        cur_len = 0
        for i in range(self._len):
            for j in range(self._len):
                if self._get_char_at(i, j) == char:
                    cur_len = self._get_line(i, j, char, 0, 1)
                    if cur_len > result_len:
                        result_len = cur_len
                    cur_len = self._get_line(i, j, char, 1, 0)
                    if cur_len > result_len:
                        result_len = cur_len
                    cur_len = self._get_line(i, j, char, 1, 1)
                    if cur_len > result_len:
                        result_len = cur_len
                    cur_len = self._get_line(i, j, char, 1, -1)
                    if cur_len > result_len:
                        result_len = cur_len
        return result_len                    
                    
    def _get_line(self, a, b, char, mod_a, mod_b):
        result_len = 0
        for i in range(self.winning_line):
            if (a + i*mod_a) < self._len and (a + i*mod_a) > -1 and (b + i*mod_b) < self._len and (b + i*mod_b) > -1 \
            and self._get_char_at(a + i*mod_a, b + i*mod_b) == char:
                result_len += 1
            else:
                break
        return result_len

class Game:
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

    @staticmethod
    def print_rules():
        print("Ход задаётся 2мя координатами через пробел от 1 до длины поля, первое число по вертикали, второе - по горизонтали")
        print("Если Вы хотите закончить игру - введите что-то отличное от 2х чисел, потребуется подтверждение")

    def __init__(self, player1, player2):
        Game.print_rules()
        self.player1 = player1
        self.player2 = player2

    def _game_begin(self):
        print("Введите желаемую длину поля (меньше 100):")
        length = int(input())
        self.board = Board(length)
        self._play()
        self.start_game()

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

    def _play(self):
        while True:
            if not self._make_turn(self.player1, self.player2, 'x'):
                break
            if not self._make_turn(self.player2, self.player1, 'o'):
                break
class Player:
    def make_turn(self, board, char):
        pass

    def __init__(self, name):
        self.name = name

class HumanPlayer(Player):
    def make_turn(self, board, char):
        print(board)
        print(self.name + ", введите Ваш ход (exit чтобы закончить):")
        turn = input()
        if turn == 'exit':
            return False
        else:
            return turn

class AIPlayer(Player):
    def make_turn(self, board, char):
        print(board)
        list_turns = []
        for i in range(board._len):
            for j in range(board._len):
                list_turns.append((i, j, self._get_weight(board, i, j, char, 'x' if char == 'o' else 'o')))
        
        best_turn = (-1, -1, 0)
        for i in list_turns:
            if i[2] > best_turn[2]:
                best_turn = i
        return str(best_turn[0]+1) + ' ' + str(best_turn[1]+1)


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

    def _wl(self, board, a, b, char, char2, mod_a, mod_b):
        result = 0.1
        last_char = ''
        for i in range(1, 3):
            if a+i*mod_a >= board._len or a+i*mod_a < 0 or b+i*mod_b >= board._len or b+i*mod_b < 0:
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