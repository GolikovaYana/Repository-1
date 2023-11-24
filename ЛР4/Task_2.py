# TODO импортировать необходимые молули
import csv
import json
import os.path

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task(path_input, path_output) -> None:
    with open(path_input, 'rt', newline='\n') as file:
        dict_csv = [line for line in csv.DictReader(file, delimiter=',')]
    f = open(path_output, 'w')
    f.write(json.dumps(dict_csv, indent=4))
    f.close

path_input_1 = os.path.abspath(INPUT_FILENAME)
path_output_2 = os.path.abspath(OUTPUT_FILENAME)

if __name__ == '__main__':
    # Нужно для проверки
    task(path_input_1, path_output_2)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
