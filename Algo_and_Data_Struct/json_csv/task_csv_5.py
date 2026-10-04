import csv

# Написать программу,
# которая объединяет несколько CSV файлов с одинаковыми заголовками в один файл.

if __name__ == '__main__':
    with open('file1.csv', mode='r', encoding='utf-8') as file1, \
            open('file2.csv', mode='r', encoding='utf-8') as file2:
        csv_reader_1 = csv.DictReader(file1, delimiter=',')
        csv_reader_2 = csv.DictReader(file2, delimiter=',')
        merged = [*csv_reader_1, *csv_reader_2]
    with open('file_merged.csv',
              mode='w',
              newline='',
              encoding='utf-8') as file:
        writer = csv.DictWriter(file,
                                fieldnames=merged[0].keys(),
                                delimiter=',')
        writer.writeheader()
        writer.writerows(merged)
