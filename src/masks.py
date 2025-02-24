import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает его маску"""

    logger.info(f'Начало работы функции "get_mask_card_number" с номером карты {card_number}')
    if not card_number or card_number.isspace() or card_number.isalpha():
        logger.error('Проверка на отсутствие номера карты: "Номер карты отсутствует"')
        return "Номер карты отсутствует"

    else:
        digit_card_number = ""
        for element in card_number:
            if element.isdigit():
                digit_card_number += element
                masket = f"{digit_card_number[:4]} {digit_card_number[4:6]}** **** {digit_card_number[-4:]}"
        logger.info(f'Успешное завершение функции "get_mask_card_number" с маской номера {masket}')
    return masket


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info(f'Начало работы функции "get_mask_account" c номером счета {account_number}')
    if not account_number or account_number.isspace() or account_number.isalpha():
        logger.error('Проверка на отсутствие номера счета: "Номер счета отсутствует"')
        return "Номер счета отсутствует"

    else:
        digit_account_number = ""
        for element in account_number:
            if element.isdigit():
                digit_account_number += element
        logger.info(f'Успешное завершение функции "get_mask_account" с маской счета **{digit_account_number[-4:]}')
    return f"**{digit_account_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("54737384584945"))
    print(get_mask_account("54345678900098765466"))
