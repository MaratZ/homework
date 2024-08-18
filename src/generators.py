from typing import Iterator

import pytest


def filter_by_currency(transaction_list: list[dict], code_of_currency: str) -> Iterator:
    """Функция возвращает итератор, где валюта соответствует заданной в параметре"""
    if len(transaction_list) > 0:
        for transaction in transaction_list:
            if transaction["operationAmount"]["currency"]["code"] == code_of_currency:
                yield transaction
    elif len(transaction_list) < 0:
        raise StopIteration("Ввели пустой список!")
    elif transaction_list == list():
        raise AssertionError("Ввели пустой список!")


# usd_transactions = filter_by_currency(transactions, "USD")

# for item in range(2):
#     print(next(usd_transactions))
# list_of_results = list()
#     for transaction in transaction_list:
#         if transaction["operationAmount"]["currency"]["code"] == code_of_currency:
#             yield transaction
#             list_of_results.append(transaction)
#     if len(list_of_results) <= 0:
#         raise StopIteration("Ввели пустой список!")