from core.notes import Notes
class View:
    def run(list):
        print("Доступные команды:\nAdd - создать заметку"
              "\nEdit-редактировать заметку\nRead-прочитать все заметки"
              "\nDelete-удалить заметку\nExit-выход")
        while True:
            command = input()
            if command == 'add':
                # id = int(input("Введите id заметки: "))
                head = input("Введите заголовок заметки: ")
                content = input("Введите содержание заметки: ")
                Notes.add(list,head,content)
            elif command == 'edit':
                id = int(input('Введите ID заметки: '))
                Notes.edit(list,id,input('Введите новый заголовок: '), input('Введите новое содержание заметки: '))
            elif command == 'delete':
                id = int(input('Введите ID заметки: '))
                Notes.delete(list,id)
            elif command == 'read':
                Notes.read(list)
            elif command == 'exit':
                break
            else:
                print('Введена неверная команда')
    if __name__ == '__view__':
        run()