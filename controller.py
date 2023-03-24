import view
import model

def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1: # Открыть файл
                model.open_file()
                view.show_massage('Файл успешно открыт!')
            case 2: # Сохранить файл
                model.save_file()
                view.show_massage('Файл успешно сохранен!')
            case 3: # Показать контакты
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4: # Добавить контакт
                contact = view.add_contact()
                model.add_contact(contact)
            case 5: # Изменить контакт
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_massage(f'Контакт {model.get_phone_book()[index - 1].get("name")} успешно изменен!')
            case 6: # Найти контакт
                search = view.input_search('Введите искомый элемент')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контакты не найдены!')
            case 7: # Удалить контакт
                search = view.input_search('Введите имя для удаления: ')
                model.dell_contact(search)
                view.show_massage(f'Контакт {search} удален!')
            case 8: # Выход
                return

