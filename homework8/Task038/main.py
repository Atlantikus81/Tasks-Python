# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
# 1. Открыть файл
# 2. Сохранить файл
# 3. Просмотреть контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def show_all():
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for i in data:
        print(i)


def adding_contact():
    data = input('Введите фамилию имя, номер телефона, комментарий через "; ": ')
    with open('sample.txt', 'a', encoding='UTF-8') as file:
        file.write(data + '\n')


def editing_contact():
    with open('sample.txt', 'r', encoding='utf8') as file:
        data = file.readlines()
    search = input('Введите поисковый запрос: ')
    new_entry = input('Введите новую запись: ')
    with open('sample.txt', 'w', encoding='utf8') as file1:
        for data_str in data:
            if search.lower() in data_str.lower():
                file1.write(new_entry + '\n')
            else:
                file1.write(data_str)


def search_contact():
    with open('sample.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
    search = input('Введите поисковый запрос: ')
    count = 0
    for data_str in data:
        if search.lower() in data_str.lower():
            count += 1
            print(data_str)
    if count == 0:
        print('Такой записи не существует!')


def deleting_contact():
    with open('sample.txt', 'r', encoding='utf8') as file:
        data = file.readlines()
    search = input('Введите поисковый запрос: ')
    with open('sample.txt', 'w', encoding='utf8') as file1:
        for data_str in data:
            if search.lower() in data_str.lower():
                data.remove(data_str)
            else:
                file1.write(data_str)


while True:
    print('----------------------------\n'
          'Меню\n'
          '----------------------------\n'
          '1. Показать весь справочник\n'
          '2. Добавить новый контакт\n'
          '3. Редактировать контакт\n'
          '4. Найти контакт\n'
          '5. Удалить контакт\n'
          '6. Выход\n'
          '----------------------------\n')
    menu_number = int(input('Выберите пункт меню: '))
    print('----------------------------')
    if menu_number == 1:
        show_all()
    if menu_number == 2:
        adding_contact()
    if menu_number == 3:
        editing_contact()
    if menu_number == 4:
        search_contact()
    if menu_number == 5:
        deleting_contact()
    if menu_number == 6:
        break