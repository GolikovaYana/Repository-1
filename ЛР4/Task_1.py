# TODO решите задачу
import json
import os.path

def task(file_path) -> float:
    with open(file_path, 'rt') as file:
        data = json.load(file)
    result = round(sum(item['score'] * item['weight'] for item in data), 3)
    return result

path = os.path.abspath('input.json')

print(task(path))
