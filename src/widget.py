from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card: str) -> str:
    """Функция принимает на вход номер карты или счета и возращает их маску"""
    bank_account = "Счет"
    index_account_card = account_card.find(bank_account)
    list_account_card = account_card.split(" ")
    if index_account_card == -1:
        list_account_card[-1] = get_mask_card_number(list_account_card[-1])
        mask_card_account = " ".join(list_account_card)
        return mask_card_account
    else:
        list_account_card[-1] = get_mask_account(list_account_card[-1])
        mask_score_account = " ".join(list_account_card)
        return mask_score_account


def get_date(date: str) -> str:
    """Функция которая принимает на вход строку с датой в формате
    2024-03-11T02:26:18.671407 и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    if date == '':
        return ''
    else:
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

#def get_date(date:str) -> str:
    #date_format = date[0:10].split("-")
    #return "-".join(date_format[::-1])
#print(get_date(""))