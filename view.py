import text_filds


def main_menu() -> int: # меню
    print(text_filds.main_menu)
    lenght_menu = len(text_filds.main_menu.split('\n')) - 1
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= lenght_menu:
            return int(choice)
        else:
            print(f'Введите ЧИСЛО от 1 до {lenght_menu}')


def show_contacts(book: list[dict], error_massage: str): # показать контакт
    if not book:
        print(error_massage)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"): <20} '
                  f'{contact.get("phone"): <20} '
                  f'{contact.get("comment"): <20}')
        return True


def add_contact() -> dict: # добавить контакт
     name = input('Введите имя: ')
     phone = input('Введите номер телефона: ')
     comment = input('Введите комментарий: ')
     return {'name': name, 'phone': phone, 'comment': comment}


def input_index(massege: str):
    return int(input(massege))


def input_search(massege):
    return input(massege)


def change_contact(book: list[dict], index: int): # изменить контакт
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index - 1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index - 1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index - 1].get('comment')}


def show_massage(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))
