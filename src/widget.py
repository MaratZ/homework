from src.masks import get_mask_account, get_mask_card


def mask_account_card(number: str) -> str:
    """Функция для маскировки счетов и карт"""
    if number.lower().startswith('счет'):
        return f"Счет {get_mask_account(number)}"
    else:
        cards = get_mask_card(number[-16:])
        new_card = number.replace(number[-16:], cards)
    return new_card


print(mask_account_card('Счет 73654108430135874305'))
print(mask_account_card('Maestro 7000792289606361'))
print(mask_account_card('Visa Platinum 7000792289606361'))


def get_date(date: str) -> str:
    """Функция преобразования даты и времени"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    
    
print(get_date('2024-07-11T02:26:18.671407'))


#if __name__ == '__main__':
    #print(get_mask_card('Счет 12345678901234567890'))
    #print(get_mask_card('Visa Platinum 1234567890123456'))