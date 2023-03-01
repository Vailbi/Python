


def inputText():
    with open('file.txt', 'a') as data:
        # data.write('\n')
        data.writelines('\n' + input('Введите Фамилию Имя отчество телефон через пробел: '))



def printText():
    data = open('file.txt', 'r')
    for line in data:
        print(line)
    data.close()

def findText():

    data = open('file.txt', 'r')
    text = input('Введите данные для поиска: ')
    for line in data.readlines():
        if text in line.split():
            print(line)

    data.close()


def changeValue():
    with open('file.txt', 'r+') as data:
        tst = [line.split() for line in data.readlines()]  # создание списка из строки файла [ff,ff,ff]
        # print(tst)
        change = input('что найти?')
        for i in tst:
            if change in i:
                print('Введите 0 - если хотите изменить Фамилию'
                      'Введите 1 - если хотите изменить Имя'
                      'Введите 2 - если хотите изменить Отчество'
                      'Введите 3 - если хотите изменить номер')

        data.seek(0)
        for i in tst:
            data.writelines('\n' + ' '.join(i))
            #data.write('\n')



def delValue():
    return 1


def Select_in_rows(arr,x):

 l,m


def main_menu():
    while True:
        print('Выберите режим работы справочника:\n'
                  'Введите 1 - Для записи данных\n'
                  'Введите 2 - Для отображения всех данных\n'
                  'Введите 3 - Для поиска данных\n'
                  'Введите 4 - Для изменения данных\n'
                  'Введите 5 - Для удалению данных\n'
                  'Введите 0 - Для выхода из программы\n')
        num = input()
        if num == '1':
            inputText()
        elif num == '2':
            printText()
        elif num == '3':
            findText()
        elif num == '4':
            changeValue()
        elif num == '5':
            delValue()
        elif num == '0':
            quit()
        else:
            print('Неверный ввод')


main_menu()
# findText()




# inputText()
# printText()
# checkText(input('Введите данные'))