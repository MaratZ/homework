def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    7000 79** **** 6361"""
    if len(str(card_number)) != 16:
        raise ValueError("Неправильный номер карты")
    return f"{int(str(card_number)[:4])} {int(str(card_number)[4:6])}** **** {int(str(card_number)[12:])}"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    **4305"""
    if len(str(account_number)) != 20:
        raise ValueError("Неправильный номер счета")
    return f"**{int(str(account_number)[-4:])}"