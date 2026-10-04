import json
import random
# Преобразуйте JSON-объект,
# содержащий список температур за месяц,
# в словарь, где ключами будут даты, а значениями — температуры.


def generate_temperatures() -> list:
    temps = [random.randint(-5, 15) for i in range(30)]
    return temps


def fill_temperature_json(temps: list) -> None:
    with open('temps.json', mode='w', encoding='utf-8') as file:
        json.dump({'temps': temps}, file, indent=4)


def make_month_dict_from_json() -> dict:
    with open('temps.json', mode='r', encoding='utf-8') as file:
        temps = json.load(file)
    temps_dict = {day: temp for day, temp in enumerate(temps['temps'], start=1)}
    return temps_dict


def json_output() -> None:
    temps = generate_temperatures()
    fill_temperature_json(temps)
    temps_dict = make_month_dict_from_json()
    print(temps_dict)


if __name__ == '__main__':
    json_output()
