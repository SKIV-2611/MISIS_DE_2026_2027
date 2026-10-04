import csv
# Создать программу,
# которая записывает список словарей с информацией о книгах в CSV файл.

books = [
    {'title': 'Война и мир', 'author': 'Толстой', 'year': 1869},
    {'title': '1984', 'author': 'Оруэлл', 'year': 1949}
]

if __name__ == '__main__':
    fieldnames = books[0].keys()
    with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(f=file,
                                    fieldnames=fieldnames,
                                    delimiter=',')
        csv_writer.writeheader()
        csv_writer.writerows(books)
