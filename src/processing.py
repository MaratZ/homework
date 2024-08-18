def filter_by_state(list_of_dictionaries: list, key: str = "EXECUTED") -> list:
    """функция принимает список словарей и опционально значение для ключа state (по умолчанию
    'EXECUTED'), возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    for i in list_of_dictionaries:
        if not i.get("state"):
            raise ValueError("Отсутствует ключ для фильтра")
    # new_list_of_dictionaries = []
    # for i in list_of_dictionaries:
    #    if i.get('state') == key:
    #        new_list_of_dictionaries.append(i)
    return [i for i in list_of_dictionaries if i.get("state") == key]


def sort_by_date(list_dictionaries: list, keys: bool = True) -> list:
    """функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)."""
    # sort_list = sorted(list_dictionaries, key=lambda list_dictionaries: list_dictionaries['date'], reverse=keys)
    # return sort_list
    return sorted(list_dictionaries, key=lambda list_dictionaries: list_dictionaries["date"], reverse=keys)