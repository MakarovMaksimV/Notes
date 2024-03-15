import datetime
from repo.repository import Repository
class Notes:
    def add(list, head, content, date = datetime.datetime.now()):
        id = len(list) + 1
        note = {'id': id, 'head': head, 'content': content, 'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        list.append(note)
        Repository.save(list)
    def read(list):
        Repository.read(list)
    def edit(list,new_id,new_head,new_content):
        note_index = -1
        for index, note in enumerate(list):
            if note['id'] == id:
                note_index = index
                break
        if note_index != -1:
            list[note_index]['head'] =  new_head
            list[note_index]['content'] =  new_content
            list[note_index]['date'] =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            Repository.save(list)
            print("Заметка отредактирована")
        else:
             print("Заметка не найдена")

    def delete(list,id):
        for i, note in enumerate(list):
            if int(note['id']) == id:
                list.pop(i)
                Repository.save(list)
                print("Заметка удалена")

                    


              

              
