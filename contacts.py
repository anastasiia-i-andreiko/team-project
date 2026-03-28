contacts = []

while True:
    print("\nВаріанти: add / show / exit")
    choice = input("Виберіть дію: ").lower()

    if choice == "add":
        name = input("Введіть ім'я: ")
        number = input("Введіть номер: ")
        contacts.append(f"{name} - {number}")
        print("Контакт додано")

    elif choice == "show":
        if not contacts:
            print("Список контактів порожній")
        else:
            print("\nКонтакти:")
            for c in contacts:
                print(c)

    elif choice == "exit":
        print("До зустрічі")
        break
    else:
        print("Невірна команда, спробуйте ще раз")