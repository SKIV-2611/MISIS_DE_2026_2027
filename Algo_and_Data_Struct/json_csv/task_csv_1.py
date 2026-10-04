import csv
# Написать программу, которая читает CSV файл со списком студентов и их оценок,
# выводит содержимое на экран.

if __name__ == '__main__':
    with open('students.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        for row in csv_reader:
            print(row)
