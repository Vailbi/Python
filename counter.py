import csv
from tempfile import NamedTemporaryFile
import shutil

# def create_id():
#     i = 0
#     def func():
#         nonlocal i
#         i += 1
#         return i
#
#     return func
def read_csv():
    with open('note.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for i in reader:
            print(*i)



def delete_in_cvs():
    filename = 'note.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False) # cоздает временный именной файл
    read_csv()
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






delete_in_cvs()


def get_id():
    with open('note.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        load = list(reader)[-1:][0][0]
        if load == 'id':
            load = 0
        else:
            load = int(load) + 1
    return str(load)


def change_text_in_cvs():
    filename = 'note.csv'
    tempfile = NamedTemporaryFile('w+t', newline='', delete=False) # cоздает временный именной файл
    read_csv()
    with open(filename, 'r', newline='') as file, tempfile:
        reader = csv.reader(file)
        writter = csv.writer(tempfile)
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
                print('Старое название:', temp[1])
                new_main = input('Введите новое название: ')
                temp.pop(1)
                temp.index(new_main, 1)
            elif num == '2':
                pass
            elif num == '0':
                break
            else:
                print('Неверный ввод')
