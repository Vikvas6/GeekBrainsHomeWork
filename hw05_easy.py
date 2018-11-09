# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
def create_dir(dirname):
        dir_path = os.path.join(os.getcwd(), dirname)
        try:
                os.mkdir(dir_path)
                print ('Успешно создано')
        except Exception:
                print ('Невозможно создать')
#'''
if __name__ == '__main__':
        for i in range(9):
                create_dir('dir_{}'.format(i+1))
#'''
def delete_dir(dirname):
        dir_path = os.path.join(os.getcwd(), dirname)
        try:
                os.rmdir(dir_path)
                print ('Успешно удалено')
        except Exception:
                print ('Невозможно удалить')
#'''
if __name__ == '__main__':
        for i in range(9):
                delete_dir('dir_{}'.format(i+1))
#'''

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

#'''
def lis_dir():
        contains = os.listdir()
        for f in contains:
                if os.path.isdir(os.path.join(os.getcwd(), f)):
                        print(f)
#'''

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

#'''
def mk_copy():
        cur_dir, cur_file = os.path.split(__file__)
        open(os.path.join(cur_dir, 'Copy_Of_' + cur_file), 'w', encoding='utf-8').write(open(cur_file, 'r', encoding='utf-8').read())
#'''