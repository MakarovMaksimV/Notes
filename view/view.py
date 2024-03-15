import datetime

from core.notes import Notes
class View:
    def run(list):
        print("Доступные команды:\nAdd - создать заметку"
              "\nEdit-редактировать заметку\nRead-прочитать все заметки"
              "\nDelete-удалить заметку\nExit-выход")
        while True:
            print("Введите команду: ")
            command = input()
            if command == 'add':
                head = input("Введите заголовок заметки: ")
                content = input("Введите содержание заметки: ")
                Notes.add(list,head,content)
            elif command == 'edit':
                id = int(input('Введите ID заметки: '))
                head = input('Введите новый заголовок: ')
                content = input('Введите новое содержание заметки: ')
                Notes.edit(list,id,head,content)
            elif command == 'delete':
                id = int(input('Введите ID заметки: '))
                Notes.delete(list,id)
            elif command == 'read':
                print ("Для чтения всех заметок введите - all")
                id = input('Введите ID заметки: ')
                Notes.read(list,id)
            elif command == 'exit':
                break
            else:
                print('Введена неверная команда')
    if __name__ == '__view__':
        run()