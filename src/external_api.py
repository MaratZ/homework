import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
values = os.getenv("PASSWORD")
keys = os.getenv("API_KEY")
headers = {keys: values}


# Обозначаем переменную, содержащую информацию о транзакции

transaction = {
    "id": 41428829,
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {"name": "USD", "code": "USD"},
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "RUB"},
    },
    "description": "\u041f\u0435\u0440\u0435\u0432\u043e\u0434"
    " \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438",
    "from": "MasterCard 7158300734726758",
    "to": "\u0421\u0447\u0435\u0442 35383033474447895560",
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

def currency_conversion(transaction: Any) -> Any:# type: ignore
    """Функция конвертации"""
    amout = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    payload = {}
    response = requests.get(url, headers={"apikey": values}, data=payload)
    result = response.json()
    return result["result"]