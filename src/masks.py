def mask_card(card_number: str) -> str | None:
    """Функция маскировки карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        return None


def mask_account(acc_number: str) -> str | None:
    """Функцию маскировки номера банковского счета"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        return None


def get_mask_account_card():
    return None