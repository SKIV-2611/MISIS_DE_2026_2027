from task_json_5_read import read_json


def create_wrong_json(file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write('{\n  "name": \'Ivan"\n  }\n')


def main() -> None:
    create_wrong_json('disformatted.json')

    data = read_json('disformatted.json')


if __name__ == '__main__':
    main()
