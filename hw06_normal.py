# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

#Это будет основной класс, через объект этого класса мы будем получать всю информаци.
#Уникальность классов в школе обеспечивается с помощью словоря - если добавить класс с существующим номером, он перезапишется
class Shkola:
    def __init__(self, klasses={}):
        self.klasses = klasses

    def add_class(self, klass):
        self.klasses[klass.number] = klass

    # 1. Получить полный список всех классов школы
    def get_klasses(self):
        list_klass_names = []
        for k in self.klasses:
            list_klass_names.append(self.klasses[k].number)
        return list_klass_names
    
    # 2. Получить список всех учеников в указанном классе
    def get_ucheniki(self, klass):
        return self.klasses[klass.number].get_ucheniki()

    # 3. Получить список всех предметов указанного ученика 
    def get_uchenik_predmets(self, uchenik):
        for k in self.klasses:
            if self.klasses[k].is_uchenik_v_klasse(uchenik):
                return self.klasses[k].uchit_dict.keys()

    # 4. Узнать ФИО родителей указанного ученика
    # Придётся поискать ученика по школе
    def get_roditel_names(self, uchenik):
        for k in self.klasses:
            if self.klasses[k].is_uchenik_v_klasse(uchenik):
                return self.klasses[k].get_roditel_names(uchenik)
        return []

    # 5. Получить список всех Учителей, преподающих в указанном классе
    def get_klass_uchitels(self, klass):
        list_uchitels = []
        for u in self.klasses[klass.number].uchit_dict:
            list_uchitels.append(self.klasses[klass.number].uchit_dict[u].get_full_name())
        return list_uchitels

        
#Класс для классов, основа - номер
#Уникальность учителя для предмета обеспечивается словарём - 
#при попытке добавить учителя по существующему предмету старый учитель перезапишется
class Klass:
    def __init__(self, number, ucheniki=[], uchit_dict={}):
        self.number = number
        self.ucheniki = ucheniki
        self.uchit_dict = uchit_dict
        
    def add_uchenik(self, uchenik):
        self.ucheniki.append(uchenik)

    def add_uchitel(self, uchitel):
        self.uchit_dict[uchitel.predmet] = uchitel

    def get_ucheniki(self):
        list_ucheniki = []
        for u in self.ucheniki:
            list_ucheniki.append(u.get_name())
        return list_ucheniki

    def is_uchenik_v_klasse(self, uchenik):
        for u in self.ucheniki:
            if u.is_equal(uchenik):
                return True
        return False

    def get_roditel_names(self, uchenik):
        for u in self.ucheniki:
            if u.is_equal(uchenik):
                return [u.mama.get_full_name(), u.papa.get_full_name()]
        return []


#Базовый класс Человек для хранения имени и сравнения людей 
#(считаем, имя-фамилия-отчество уникальны)
class Man:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
    
    def get_name(self):
        return '{} {}.{}.'.format(self.last_name, self.first_name[0], self.middle_name[0])
    
    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)
    
    def is_equal(self, other):
        if self.first_name == other.first_name and self.middle_name == other.middle_name and self.last_name == other.last_name:
            return True
        return False

class Roditel(Man):
    pass

class Uchenik(Man):
    def __init__(self, first_name, middle_name, last_name, mama, papa):
        super().__init__(first_name, middle_name, last_name)
        self.mama = mama
        self.papa = papa

class Uchitel(Man):
    def __init__(self, first_name, middle_name, last_name, predmet):
        super().__init__(first_name, middle_name, last_name)
        self.predmet = predmet



MamaIvanova = Roditel('Раиса', 'Михайловна', 'Иванова')
PapaIvanova = Roditel('Андрей', 'Алексеевич', 'Иванов')
Ivanov = Uchenik('Олег', 'Андреевич', 'Иванов', MamaIvanova, PapaIvanova)

MamaPetrova = Roditel('Татьяна', 'Константиновна', 'Петрова')
PapaPetrova = Roditel('Дмитрий', 'Александрович', 'Петров')
Petrov = Uchenik('Евгений', 'Дмитриевич', 'Петров', MamaPetrova, PapaPetrova)

MatemIlin = Uchitel('Николай', 'Аркадьевич', 'Ильин', 'математика')
RuskiiKomarova = Uchitel('Жанна', 'Владимировна', 'Комарова', 'русский язык')

Klass5A = Klass('5А')
Klass5A.add_uchenik(Ivanov)
Klass5A.add_uchenik(Petrov)
Klass5A.add_uchitel(MatemIlin)
Klass5A.add_uchitel(RuskiiKomarova)

Shkola34 = Shkola()
Shkola34.add_class(Klass5A)

print(Shkola34.get_klasses())
print(Shkola34.get_ucheniki(Klass('5А')))
print(Shkola34.get_uchenik_predmets(Man('Олег', 'Андреевич', 'Иванов')))
print(Shkola34.get_roditel_names(Man('Олег', 'Андреевич', 'Иванов')))
print(Shkola34.get_klass_uchitels(Klass('5А')))