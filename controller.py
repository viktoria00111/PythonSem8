import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Выберите нужную вам команду и введите соответствующую цифру: ')
        print()
        if answer == '1':
            data = model.storage()
            view.show_contacts(data)
        elif answer == '2':
            contact = input("Введите данные, которые нужно добавить: ")
            res = model.add_contact(contact)
            if res: 
                view.success(res)
            else: 
                view.not_success(res)
        elif answer == '3':
            contact = input("Введите данные для поиска: ")
            res = model.finder(contact)
            view.show_contacts(res)
        elif answer == '4':
            contact = input("Введите данные для поиска контакта, который требуется изменить: ")
            res = model.finder(contact)
            view.show_contacts(res)
            contact_change = input("Введите новые данные для изменения: ")
            res_change = model.changer(contact_change)
            if res_change: 
                view.success(res)
            else: 
                view.not_success(res)
        elif answer == '5':
            contact = input("Введите данные контакта, который требуется удалить: ")
            res = model.delete_cont(contact)
            view.show_contacts(res)
            if res: 
                view.success(res)
            else: 
                view.not_success(res)
        elif answer == '6':
            view.ciao()
        else:
            view.error()
        


# if __name__ == "__main__":
#     start()