import os
import time

from dotenv import load_dotenv
from csv import DictReader, DictWriter

from alive_progress import alive_bar


def main():
    in_filename = os.getenv('input_filename', 'in.csv')
    if not os.path.exists(in_filename):
        return print(f'Файла {in_filename} не существует!')
    out_filename = os.getenv('output_filename', 'out.csv')
    delimiter = os.getenv('delimiter', ';')
    with open(in_filename, encoding='utf-8') as in_file:
        first_line = in_file.readline().strip()
        if not first_line:
            return print(f'Файл {in_filename} пуст!')
        fieldnames = first_line.split(';')
        with open(out_filename, 'w', newline='', encoding='utf-8') as out_file:
            writer = DictWriter(out_file, fieldnames, delimiter=';')
            writer.writeheader()
            with alive_bar() as bar:
                for row in DictReader(in_file, fieldnames, delimiter=delimiter):
                    for url in row.pop('URL').split(', '):
                        writer.writerow({**row, 'URL': url})
                    bar()


if __name__ == '__main__':
    load_dotenv()
    main()
