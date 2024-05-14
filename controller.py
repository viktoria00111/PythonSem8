import os

def add_contact():# добавление
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    patronymic = input("Enter patronymic: ")
    phone_number = input("Enter phone number: ")
    with open("phonebook.txt", "a") as f:
        f.write(f"{name},{surname},{patronymic},{phone_number}\n")
    print("Contact added successfully.")

def search_contact():# поиск
    search_key = input("Enter search key: ")
    with open("phonebook.txt", "r") as f:
        for line in f:
            if search_key in line:
                print(line)


def changer_contacts():# изменение
    with open("phonebook_changer.txt", "w") as f:
        data = f.read()
    with open("phonebook.txt", "a") as f:
        f.write(data)
    print("Contacts changeres successfully.")
    
def delete_contacts():
    with open("phonebook.txt", 'r+') as f:
        data = f.read()
    with open("phonebook_delete.txt", 'w+') as f:
        f.write(data)
    print("Contacts delete successfully.")

def main():
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete")
        print("4. Changer contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            changer_contacts()
        elif choice == "5":
             break
        else:

            #
            print("Invalid choice.")
        input("Press Enter to continue...")
        os.system("clear")

if __name__ == "__main__":    
   main()
