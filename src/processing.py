from typing import Any

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа
    state и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    filtered_operations = []
    for key in operations:
        if key.get("state") == state:
            filtered_operations.append(key)
    return filtered_operations


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список, в котором исходные
    словари отсортированы по убыванию даты
    """
    operations = sorted(operations, key=lambda new_list_of_dict: new_list_of_dict["date"], reverse=reverse)
    return operations


#print(filter_by_state(operations))