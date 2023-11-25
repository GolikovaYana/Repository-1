# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task(file_input, file_output) -> None:
    with open(file_input, 'rt', newline='\n') as file:
        dict_csv = [line for line in csv.DictReader(file, delimiter=',')]
    f = open(file_output, 'w')
    f.write(json.dumps(dict_csv, indent=4))
    f.close

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
