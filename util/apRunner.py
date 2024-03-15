import json
import os

from view.view import View

class ApRunner:
    def runner():
        file = "notes.json"
        if not os.path.exists(file):
            print("Файл не найден")
        else:
            with open(file) as f:
                data = f.read()
                if not data:
                    notes = []
                else:
                    notes = list(json.loads(data))
                View.run(notes)

