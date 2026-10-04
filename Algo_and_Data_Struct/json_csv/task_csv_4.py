import csv
# Создать программу,
# которая подсчитывает среднюю оценку по предмету
# из CSV файла с оценками студентов.

if __name__ == '__main__':
    with open('student_grades.csv',
              mode='r',
              encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        grades = [item for item in csv_reader]
    grades_by_subject = dict()
    for di in grades:
        for key, value in di.items():
            if key == 'Студент':
                continue
            if key not in grades_by_subject:
                grades_by_subject[key] = list()
            grades_by_subject[key].append(int(value))
    avg_grades_by_subject = {key: sum(value) / len(value) for key, value in grades_by_subject.items()}
    with open('avg_student_grades.csv',
              mode='w',
              newline='',
              encoding='utf-8') as file:
        writer = csv.DictWriter(f=file,
                                fieldnames=avg_grades_by_subject.keys(),
                                delimiter=',')
        writer.writeheader()
        writer.writerows([avg_grades_by_subject])
