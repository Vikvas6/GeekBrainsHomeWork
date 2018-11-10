# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.



# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        open(dir_name+'_copy', 'w', encoding='utf-8').write(open(dir_name, 'r', encoding='utf-8').read())
        print('Файл {} скопирован в файл {}'.format(dir_name, dir_name+'_copy'))
    except Exception:
        print('Создать копию файла {} не удалось'.format(dir_name))


def rm_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    print('Вы точно хотите удалить файл {}? (y/n)'.format(dir_name))
    if input() == 'y':
        try:
            os.remove(dir_name)
            print('Файл {} удалён'.format(dir_name))
        except Exception:
            print('Файл {} удалить не удалось'.format(dir_name))


#Я, видимо, немного не понял задание, но какой смысл в этой функции в такой реализации, когда на каждое действие нам нужно вызывать скрипт?
#Ведь после первого вызова с ключом cd мы перейдём в нужную папку, программа завершится и, насколько я понимаю, любая IDE вернёт нас в рабочую папку скрипта
#(во всяком случае, у меня Visual Studio Code и она меня вернула)
#Возможно, при запуске из консоли возвращения не будет, тогда, видимо, стоит добавить этот скрипт в переменную Path, чтобы не приходилось прописывать полный путь к нему
def change_dir():
    if not dir_name:
        print("Необходимо указать имя папки вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print("Переход успешно выполнен")
    except Exception:
        print("Не удалось выполнить переход")

    
def full_path_dir():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": rm_file,
    "cd": change_dir,
    "ls": full_path_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
