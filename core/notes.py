import datetime
from repo.repository import Repository
class Notes:
    def add(list, head, content, date = datetime.datetime.now()):
        id = len(list) + 1
        note = {'id': id, 'head': head, 'content': content, 'date': date.strftime('%Y-%m-%d %H:%M:%S')}
        list.append(note)
        Repository.save(list)
    def read(list,id):
        Repository.read(list,id)
    def edit(list,id,new_head,new_content):
        found = False
        for i, note in enumerate(list):
            if note['id'] == id:
                list[i]['head'] = new_head
                list[i]['content'] = new_content
                list[i]['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print("Заметка отредактирована")
                found = True
        if not found:
            print("Заметка с таким ID не найдена")
        Repository.save(list)

    def delete(list,id):
        found = False
        for i, note in enumerate(list):
            if int(note['id']) == id:
                list.pop(i)
                Repository.save(list)
                print("Заметка удалена")
                found = True
        if not found:
            print("Заметка с таким ID не найдена")

                    


              

              
