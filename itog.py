import time
import csv
from tempfile import NamedTemporaryFile
import shutil


def get_data():
    return time.strftime("%d.%m.%Y - %H:%M:%S", time.localtime())


def get_id():
    with open('note.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        load = list(reader)[-1:][0][0]
        if load == 'id':
            load = 0
        else:
            load = int(load) + 1
    return str(load)


# Создание файла нот
def note():

    with open('note.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        content = ['id', 'Название заметки', 'Текст заметки', 'Дата создания']
        writer.writerow(content)


# Cоздание записи в заметках
def add_new_note():
    main = input('Введите название заметки: ')
    text = input('Введите текст заметки')
    with open('note.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([get_id(), main, text, get_data()])


def read_csv():
    with open('note.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for i in reader:
            #print(*i)
            print(' | '.join(i))


# read_csv()


def find_text_in_csv():
    with open('note.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        text = input('Введите данные для поиска заметки(id,название заметки или фрагмент заметки): ')
        for i in reader:
            if text in i:
                print(*i)


def change_text_in_cvs():
    with open('note.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for i in reader:
            print(*i)
        find_id = input('Введите id заметки для изменения: ')
        temp = []
        for j in reader:
            for f_id in j:
                if f_id == find_id and f_id == j[0]:
                    temp.append(j)
        while True:
            print('Выберите поле для изменения:\n'
                  'Введите 1 - Для изм. названия\n'
                  'Введите 2 - Для измю текста\n'
                  'Введите 0 - Для выхода в главное меню'
                  )
            num = input()
            if num == '1':
                pass
            elif num == '2':
                pass
            elif num == '0':
                break
            else:
                print('Неверный ввод')


def delete_in_cvs():
    filename = 'note.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False) # cоздает временный именной файл

    with open(filename, 'r', newline='') as file: # здесь читаем файл по строкам (не обязательно для удобства)
        reader = csv.reader(file)
        for i in reader:
            print(*i)
    with open(filename, 'r', newline='') as file,tempfile: # тут открываем два файла сsv и времменый
        reader = csv.reader(file) # на чтение передаем цсв
        writer = csv.writer(tempfile) # на запись передаем времменый
        find_id = input('Введите id заметки для удаления: ')
        for j in reader:
            if find_id == j[0]: # если айди совпадают, то прпускаем, все остальное записываем
                continue
            else:
                writer.writerow(j)# записываем строки с другими айди
    shutil.move(tempfile.name, filename) # производим замену временного файла на основной


def main_menu():
    while True:
        print('Выберите режим работы Заметок:\n'
              'Введите 1 - Для записи данных\n'
              'Введите 2 - Для отображения всех данных\n'
              'Введите 3 - Для поиска данных\n'
              'Введите 4 - Для изменения данных\n'
              'Введите 5 - Для удалению данных\n'
              'Введите 0 - Для выхода из программы\n')
        num = input()
        if num == '1':
            add_new_note()
        elif num == '2':
            read_csv()
        elif num == '3':
            find_text_in_csv()
        elif num == '4':
            pass
        elif num == '5':
            delete_in_cvs()
        elif num == '0':
            quit()
        else:
            print('Неверный ввод')


main_menu()
