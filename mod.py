import datetime



arr = []


def prints(list_file: list[dict], msg_out_in_menu):
    ind = 1
    for dic in list_file:
        print(f'{ind}. {dic.get("name"):>5} {dic.get("time"):>50}')
        ind += 1
    input(msg_out_in_menu)


def open_note(list_file: list[dict], msg_choice_menu: str, msg_out_in_menu: str):
    choice = int(input(msg_choice_menu))

    print(list_file[choice - 1]["name"])
    print(list_file[choice - 1]["content"])
    input(msg_out_in_menu)


def changes(list_file: list[dict], msg_choice_note, msg_note_name, msg_note_content):
    choice = int(input(msg_choice_note))
    name = input(msg_note_name)
    content = input(msg_note_content)
    if len(name) > 0:
        list_file[choice - 1]['name'] = name
    if len(content) > 0:
        list_file[choice - 1]['content'] = content
    return list_file


def deletes(list_file: list[dict], msg_choice_note):
    choice = int(input(msg_choice_note))
    list_file.pop(choice - 1)


def add(list_file: list, msg_note_name, msg_note_content):
    id_note = len(list_file) + 1
    name = input(msg_note_name)
    content = input(msg_note_content)
    cur_time = datetime.datetime.today().strftime("Дата :%Y-%m-%d; Время :%H.%M.%S")
    dictt = {'id': id_note, 'name': name, 'content': content, 'time': cur_time}
    return dictt
