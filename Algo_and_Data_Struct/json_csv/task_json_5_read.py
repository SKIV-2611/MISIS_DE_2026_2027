import json


def read_json(file_name: str, encoding: str = 'utf-8') -> dict:
    """Reads JSON file error-safe (?).

    :param file_name: JSON file name
    :param encoding: JSON file encoding
    :return: Returns JSON-representing dict
    """
    try:
        with open(file_name, 'r', encoding=encoding) as file:
            data = json.load(file)
        return data
    except FileNotFoundError as fnfe:
        print(f'File {fnfe.filename} not found.')
    except json.JSONDecodeError as je:
        print(f'Incorrect JSON in file {file_name}!!!')
        print(f'{je.msg}')
    except ValueError as ve:
        print(f'Incorrect format in file {file_name}!!!')
