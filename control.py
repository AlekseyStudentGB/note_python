import json
import mod
import view
import text_rus


def start():
    current_name_file = 'data_file.json'
    try:
        with open(current_name_file, encoding='UTF-8') as file:
            list_file = json.load(file)
    except:
        with open(current_name_file, 'w', encoding="UTF-8") as file:
            list_file = []
            json.dump(list_file, file)

    while True:

        choice = view.menu()
        match choice:
            case 1:
                with open(current_name_file, 'w', encoding='utf-8') as file:
                    list_file.append(mod.add(list_file, text_rus.msg_note_name, text_rus.msg_note_content))
                    json.dump(list_file, file)
            case 2:
                mod.prints(list_file, text_rus.msg_out_in_menu)
            case 3:
                mod.open_note(list_file, text_rus.msg_choice_note, text_rus.msg_out_in_menu)
            case 4:
                mod.changes(list_file, text_rus.msg_choice_note, text_rus.msg_note_name, text_rus.msg_note_content)
            case 5:
                mod.deletes(list_file, text_rus.msg_choice_note)
                with open(current_name_file, 'w', encoding='utf-8') as file:
                    json.dump(list_file, file)
            case 6:
                break
