def read_txt(filename): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def show_menu():
    try:
        print("\nВыберите необходимое действие:")
        print("1. Отобразить весь справочник")
        print("2. Найти абонента по фамилии")
        print("3. Найти абонента по номеру телефона")
        print("4. Добавить абонента в справочник")
        print("5. Изменить данные")
        print("6. Сохранить справочник в текстовом формате")
        print("7. Закончить работу")
        choice = int(input())
        return choice
    except ValueError:
        print("Ошибка: Введите число от 1 до 7.")
        return show_menu()

def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    found_records = [record for record in phone_book if record.get('Фамилия') == last_name]
    return found_records

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record.get('Фамилия') == last_name:
            record['Телефон'] = new_number
            write_txt('phonebook.txt', phone_book)
            return f"Номер для {last_name} успешно изменен на {new_number}."
    return f"Абонент с фамилией {last_name} не найден."

def delete_by_lastname(phone_book, last_name):
    phone_book = [record for record in phone_book if record.get('Фамилия') != last_name]
    return f"Абонент с фамилией {last_name} успешно удален."

def find_by_number(phone_book, number):
    number = number.replace(" ", "")
    found_records = [record for record in phone_book if record.get('Телефон', '').replace(" ", "") == number]
    return found_records

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_record = dict(zip(fields, user_data.split(',')))
    phone_book.append(new_record)
    return "Абонент успешно добавлен."

def phonebook():
    while True:
        choice = show_menu()
        if choice == 7:
            break
        phone_book = read_txt('phonebook.txt')
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = input('Введите данные (Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 5:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 6:
            write_txt('phonebook.txt', phone_book)
            print('Справочник сохранен.')
        else:
            print('Неверный выбор. Попробуйте еще раз.')
if __name__ == "__main__":
    phonebook()