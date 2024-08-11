from src.masks import get_mask_account_card


def mask_account_card(number: str) -> str:
    #"""Функция для маскировки счетов и карт"""
    if len(number.split()[-1]) == 16:
        new_number = card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        return result
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account_card(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
    return result





def get_date(date: str) -> str:
    """Функция преобразования даты и времени"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    
    
#print(get_date('2024-07-11T02:26:18.671407'))

