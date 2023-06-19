from os import path

file_base = "base.txt"
last_id = 0
all_data = []


def check_name(name: str):
    return name.isalpha() and name[0].isupper() and name[1::].islower()


def check_phone(phone: str):
    return phone.isdigit()


fields = {
    "surname" : check_name, 
    "name": check_name, 
    "patronymic": check_name, 
    "phone_number": check_phone
    }


if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records(name=file_base):
    global last_id, all_data

    with open(name, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])


def save_all_data(name=file_base):
    with open(name, "w", encoding="utf-8") as f:
        for i in all_data:
            f.write(i + '\n')


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def get_checked_value(string: str, check_function):
    flag = True
    while flag:
        value = input(string)
        flag = not check_function(value)
        if flag:
            print("Bad value")
    return value


def add_new_contact():
    global last_id    
    new_record = [last_id + 1]
    for field in fields.items():
        new_record.append(get_checked_value(f"Enter {field[0]} ", field[1]))
    last_id = new_record[0]
    new_record = " ".join(map(str, new_record))
    with open(file_base, "a", encoding="utf-8") as f:
        f.write(new_record + '\n')


def seach_records():
    string = input("Enter the value you are looking for ")
    flag = False
    for record in all_data:
        if record.find(string) != -1:
            print(record)
            flag = True
    if not flag:
        print("Not found")


def delete_record():
    id = input("Enter the id of the record you want to delete ")
    if not id.strip().isdigit():
        print("Bad id")
        return 
    for record in all_data:
        if record.startswith(id):
            all_data.remove(record)
            save_all_data()
            return
    print("Not found")


def change_record():
    id = input("Enter the id of the record you want to change ")
    if not id.strip().isdigit():
        print("Bad id")
        return 
    for i in range(len(all_data)):
        if all_data[i].startswith(id):
            all_data[i] = change_field(all_data[i])
            break
    else:
        print("Not found")
        return
    save_all_data()

    
def change_field(record: str):
    record_mas = record.split()
    data = [*zip(range(1, 5), fields.keys(), fields.values(), record_mas[1::])]
    print(*[f'{i[0]}. {i[1]}: {i[3]}' for i in data], sep='\n')
    id = get_checked_value("Enter the number of the field to be changed ", lambda x: x.isdigit() and int(x) in range(1, 5))
    id = int(id) - 1   
    record_mas[id] = get_checked_value(f"Enter {data[id][1]} ", data[id][2])
    return ' '.join(record_mas)


def export_import():
    action =  get_checked_value("Do you want to import (i) or export (e) a file? ", lambda x: x in 'ie')
    check_file_name = path.exists if action == 'i' else lambda x: not path.exists(x)
    name = get_checked_value("Enter file name ", check_file_name)
    if action == 'i':
        read_records(name)
        save_all_data()
    else:
        save_all_data(name) 


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                seach_records()
            case "4":
                change_record()
            case "5":
                delete_record()
            case "6":
                export_import()
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()