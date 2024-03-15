import json

class Repository:
    def save(list):
        with open('notes.json','w') as f:
            json.dump(list,f)
    def read(list):
        with open('notes.json') as f:
            data = f.read()
            if not data:
                print("Заметок нет")
            else:
                list = json.loads(data)
                print(list)



        
    

        
