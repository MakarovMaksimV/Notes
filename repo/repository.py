import json

class Repository:
    def save(list):
        with open('notes.json','w') as f:
            json.dump(list,f)
    def read(list,id):
        if len(list) == 0:
            print("Заметок нет")
        else:
            if id == 'all':
                with open('notes.json') as f:
                    data = f.read()
                    list = json.loads(data)
                    print(list)
            else:
                found = False
                for i, note in enumerate(list):
                    if note['id'] == int(id):
                        print(list[i])
                        found = True
                if not found:
                    print("Заметка с таким ID не найдена")





        
    

        
