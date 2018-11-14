# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Employee:
    #функция пригодится для легкого парса таблиц в файле, без прибегания к импорту каких-либо библиотек
    #превращает большое количество пробелов в один пробел, чтобы потом по этому пробелу разбить строку на колонки
    def replace_spaces(self, ln):
        return ln.replace('     ', ' ').replace('    ', ' ').replace('   ', ' ').replace('  ', ' ').replace('\n', '')

    def __init__(self, str_data):
        str_splitted = self.replace_spaces(str_data).split(' ')
        self.first_name = str_splitted[0]
        self.last_name  = str_splitted[1]
        self.oklad      = float(str_splitted[2])
        self.position   = str_splitted[3]
        self.norma      = float(str_splitted[4])

    def get_salary(self, str_data):
        for line in str_data.split('\n'):
            str_splitted = self.replace_spaces(line).split(' ')
            if str_splitted[0] == self.first_name and str_splitted[1] == self.last_name:
                real = float(str_splitted[2])
                hour_price = self.oklad / self.norma
                if self.norma > real:
                    print(self.first_name, self.last_name, self.oklad + hour_price*(real - self.norma))
                else:
                    print(self.first_name, self.last_name, self.oklad + 2*hour_price*(real - self.norma))
                return
        print('Данные не найдены')

employees = []
with open('data/workers', 'r', encoding='utf-8') as workers:
    workers.readline()
    for line in workers:
        employees.append(Employee(line))

with open('data/hours_of', 'r', encoding='utf-8') as hours:
    hours.readline()
    all_data = hours.read()
    for e in employees:
        e.get_salary(all_data)


        