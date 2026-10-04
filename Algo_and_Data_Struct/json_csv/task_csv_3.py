import csv
# Написать программу,
# которая фильтрует CSV файл с данными о продажах,
# оставляя только записи с суммой больше 1000 рублей.

if __name__ == '__main__':
    with open('sales.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        sales_over_1000 = [item for item in csv_reader if int(item['Сумма']) > 1000]
    with open('sales_filtered.csv',
              mode='w',
              newline='',
              encoding='utf-8') as file:
        writer = csv.DictWriter(f=file,
                                fieldnames=sales_over_1000[0].keys(),
                                delimiter=',')
        writer.writeheader()
        writer.writerows(sales_over_1000)



