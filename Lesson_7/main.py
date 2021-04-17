# Файлы и JSON
from pathlib import Path
import os
import json

BASE_DIR = Path(__file__).resolve().parent

# Создать файл +
# Записать в него текст +
# Добавить в файл текст +
# Прочитать текст из файла +
# Удалить файл +

# FILENAME = BASE_DIR / "mydir" / "test.txt"

"""
    w – write (записать)
    r - read (прочесть)
    a - append (добавить)

    b - binary
"""

# FILE_DIR = FILENAME.parent

# if os.path.isfile(FILENAME):
#     file = open(FILENAME, 'r')
#     print(file.read())
#     file.close()
# else:
#     print("Файл не существет")

"""
    dict
    list
    int
    str ; '' / "" ; ""
    float

    True, False ; true, false
    None ; null
"""

obj = {
    'id': 1,
    "desc": None,
    'items': [
        {
            "name": "asdfqdwasedw",
            "age": 3000,
            "number": 3.14,
            "active": True
        },
        {
            "name": "asdfqdwasedw",
            "age": 3000,
            "number": 3.14,
            "active": False
        }
    ]
}


"""
    load - загрузить (из файла)
    loads - загрузить (из строки)

    dump - выгрузить / создать JSON (в файл)
    dumps - выгрузить / создать JSON (в строку)
"""

# json_obj = json.dumps(obj, indent=2)

# print(json_obj)

# file = open(BASE_DIR / "test.json", 'w')
# json.dump(obj, file, indent=2)
# file.close()


with open(BASE_DIR / "test.json", 'r') as file:
    res = json.load(file)

print(res['items'][0]['age'])

class JSONFile:
    def __init__(self, filename):
        self.filename = Path(filename).resolve()
        self.data = {}
        os.mkdir(self.filename.parent)

    def __enter__(self):
        return self.data

    def __exit__(self, type_, value, tb):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=2)


with JSONFile(BASE_DIR / "jsons" / "my.json") as obj:
    obj['id'] = 10
    obj['items'] = [
        {
            "name": "asdfqdwasedw",
            "age": 400,
            "number": 3.334,
            "active": True
        },
        {
            "name": "11",
            "age": 3000,
            "number": 3.14,
            "active": False
        }
    ]

