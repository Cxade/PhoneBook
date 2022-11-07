import model
import view
import os



def main_menu():
    while True:
        print(f'\nГлавное меню ({model.path}):')
        print('1. Показать контакты')
        print('2. Добавить контакт')
        print('3. Удалить контакт')
        print('4. Изменить контакт')
        print('5. Выбрать другой файл')
        print('8. Сохранить файл')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                print('\nСписок контактов:\n')
                view.printPhoneBook()
            case 2:
                add_contact()
                print('\nКонтакт добавлен\n')
            case 3:
                remove_contact()
                print('\nКонтакт удален\n')
            case 4:
                change_contact()
            case 5:
                switch_file()
            case 8:
                save_file()
                print('\nФайл сохранен!\n')
            case 0:
                break


def start():
    open_file()
    main_menu()


def open_file():
    with open(model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        model.phonebook = contacts_list


def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    model.phonebook.append(contact)
    view.printPhoneBook()


def remove_contact():
    choice = int(input('Введите позицию контакта для удаления: '))
    model.phonebook.pop(choice)
    view.printPhoneBook()


def change_contact():

    choice = int(input('Введите позицию контакта для изменения: '))
    choice2 = int(input('Что изменяем? (1-имя, 2-фамилия, 3-отчество, 4-телефон): '))

    contact = model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2-1] = input('Введите новое значение: ')
    print(contact)
    model.phonebook.insert(choice, ';'.join(contact))
    view.printPhoneBook()


def switch_file():
    a = input('Введите полное название файла: ')
    if os.path.exists(a):
        model.path = a
        open_file()
        print('Файл успешно изменён')
    else: 
        print('Проверьте правильность ввода данных')


def save_file():
    with open(model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(model.phonebook)))