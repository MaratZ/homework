import logging
import os

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)



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