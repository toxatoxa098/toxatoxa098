from typing import Union


def mask_account_card(account_card: Union[str]) -> Union[str]:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах."""

    parts = account_card.split()
    account_type = " ".join(parts[:-1])
    number = parts[-1]

    if account_type.lower().startswith("счет"):
        masked_number = f"**{number[-4:]}"
    else:
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    return f"{account_type} {masked_number}"


def get_date(line: Union[str]) -> Union[str]:
    """Функция,которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
 и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024")."""

    return f'{line[8:10]}.{line[5:7]}.{line[0:4]}'


print(mask_account_card('Счет 73654108430135874305'))
print(mask_account_card('Visa Platinum 7000792289606361'))
print(get_date("2024-03-11T02:26:18.671407"))
