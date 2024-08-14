
def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки карты"""
    return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"


def get_mask_account(acc_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    return f"{'*' * 2}{acc_number[-4::]}"

#print(get_mask_card_number("1234567891234567"))