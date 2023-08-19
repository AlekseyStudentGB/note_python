import text_rus


def menu():
    print(text_rus.menu_text)
    while True:
        choice = input(text_rus.msg_choice_menu)
        if choice.isdigit() and 0 < int(choice) < 7:
            return int(choice)


def menu_file():
    print(text_rus.menu_not_file)
    while True:
        choice = input()
        if choice.isdigit() and 0 < int(choice) < 3:
            return int(choice)
