contacts = {}

while True:
    print("\nВаріанти: add / show / delete / exit")
    choice = input("Виберіть дію: ").lower()

    if choice == "add":
        name = input("Введіть ім'я: ")
        number = input("Введіть номер: ")
        contacts[name] = number
        print("Контакт додано")

    elif choice == "show":
        if not contacts:
            print("Список контактів порожній")
        else:
            print("\nКонтакти:")
            for name, number in contacts.items():
                print(f"{name} - {number}")

    elif choice == "delete":
        name = input("Введіть ім'я для видалення: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} видалено")
        else:
            print("Контакт не знайдено")

    elif choice == "exit":
        print("До зустрічі")
        break
    else:
        print("Невірна команда, спробуйте ще раз")