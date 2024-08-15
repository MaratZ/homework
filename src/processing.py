from typing import Any

list_of_dicts = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


from typing import Iterable
from typing import Any


def filter_by_state(filter_state: Iterable, state="EXECUTED") -> Any and Iterable:
    """Функция принимает список словарей и возвращает новый список словарей содержащий только
    те словари, у которых ключ state соответствует указанному значению"""
    new_filter_state = []

    for dictionary_state in filter_state:
        if dictionary_state["state"] == state:
            new_filter_state.append(dictionary_state)

    return new_filter_state


def sort_by_date(sort_state: list[dict[str, Any]], reverse=False) -> list[dict[str, Any]]:
    """Функция возвращает новый список отсортированный по дате"""
    sorted_state_date = sorted(sort_state, key=lambda sort_state: sort_state["date"], reverse=reverse)
    return sorted_state_date

print(f'{filter_by_state(list_of_dicts)}')
print(f'{sort_by_date(list_of_dicts)}')