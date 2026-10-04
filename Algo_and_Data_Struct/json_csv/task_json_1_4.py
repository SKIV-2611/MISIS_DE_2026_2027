import json
from task_json_utility import template_json_task_output

STUDENT_DATA_FILE = 'student_data.json'
BOOK_CATALOG_FILE = 'book_catalog.json'


# Task 1 functions
def get_student_dict() -> dict:
    """Returns custom student data dict."""
    return {
        'name': 'Dio',
        'age': 26,
        'courses': ['Analysis', 'Algebra', 'Discrete Maths', 'History', 'Algorithms'],
        'marks': [3, 4, 5, 4, 4]
    }


def student_dict_to_json() -> str:
    """Returns JSON-formatted custom student str."""
    student_dict = get_student_dict()

    student_json = json.dumps(student_dict, indent=2)
    return student_json


def print_student_json() -> None:
    student_json = student_dict_to_json()
    print(student_json)
# Task 1 end


# Task 2 functions
def get_student_name(file_name: str) -> str:
    """Returns student name from JSON."""
    student = read_student_from_json(file_name)

    return student.get('name', '')


def print_student_name(file_name: str) -> None:
    """Prints student name."""
    name = get_student_name(file_name)
    print(name)
# Task 2 end


# Utility
def write_student_to_json(student: dict | str, file_name: str = STUDENT_DATA_FILE) -> None:
    """Writes a dict or str representing student to JSON file."""
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(student, file, ensure_ascii=False)


# Utility
def read_student_from_json(file_name: str = STUDENT_DATA_FILE) -> dict:
    """Reads student data from JSON file and returns it as a dict."""
    with open(file_name, 'r', encoding='utf-8') as file:
        student = json.load(file)
    return student


# Task 3 functions
def add_student_email(file_name: str = STUDENT_DATA_FILE) -> None:
    """Adds student email to JSON file."""
    student_dict = read_student_from_json(STUDENT_DATA_FILE)
    student_dict['email'] = 'dio.brando@mail.ru'
    write_student_to_json(student_dict, STUDENT_DATA_FILE)


def modify_student() -> None:
    """Runs task 3"""
    student = get_student_dict()
    write_student_to_json(student)

    add_student_email(STUDENT_DATA_FILE)

    student = json.dumps(read_student_from_json(), indent=2)
    print(student)
# Task 3 end


# Task 4 functions
def create_book_json(file_name: str = BOOK_CATALOG_FILE) -> None:
    """Writes book dict to JSON file."""
    books = [
        {
            "title": 'Nine Princes in Amber',
            "author": 'Roger Zelyazny',
            "publication_year": 1970
        },
        {
            "title": 'The Guns of Avalon',
            "author": 'Roger Zelyazny',
            "publication_year": 1972
        },
        {
            "title": 'The Werewolf Principle',
            "author": 'Clifford Simak',
            "publication_year": 1967
        },
        {
            "title": 'White Fang',
            "author": 'Jack London',
            "publication_year": 1906
        },
        {
            "title": 'All Flesh is Grass',
            "author": 'Clifford Simak',
            "publication_year": 1965
        },
    ]
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False)


def find_books_by_author(file_name: str, author: str) -> list:
    """Returns all books of the author if found."""
    with open(file_name, 'r', encoding='utf-8') as file:
        library = json.load(file)
    result = [book for book in library if book.get('author', '').lower() == author.lower()]
    return result


def print_found_books() -> None:
    """Runs task 4."""
    create_book_json(BOOK_CATALOG_FILE)
    simak_books = find_books_by_author(BOOK_CATALOG_FILE, 'Clifford Simak')
    print(simak_books)
# Task 4 end


def json_output() -> None:
    task_1_desc = 'Создайте словарь с информацией о студенте (имя, возраст, оценки) и преобразуйте его в JSON-формат.' \
                  ' Выведите результат в консоль.'
    template_json_task_output(task_number=1,
                              task_desc=task_1_desc,
                              function=print_student_json)

    task_2_desc = 'Дан файл data.json. Напишите программу, которая прочитает файл и выведет имя студента.'
    template_json_task_output(task_number=2,
                              task_desc=task_2_desc,
                              function=print_student_name,
                              file_name='data.json')

    task_3_desc = 'Добавьте в JSON-объект новое поле email и обновите файл на диске.'
    template_json_task_output(task_number=3,
                              task_desc=task_3_desc,
                              function=modify_student)

    task_4_desc = 'Создайте JSON-файл, ' \
                  'содержащий список словарей с информацией о книгах (название, автор, год издания).' \
                  ' Добавьте функцию для поиска книг по автору.'
    template_json_task_output(task_number=4,
                              task_desc=task_4_desc,
                              function=print_found_books)


if __name__ == '__main__':
    json_output()
