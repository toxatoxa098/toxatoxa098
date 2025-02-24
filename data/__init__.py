import os
import json

path = os.getcwd()
print(path)

def transactions_filtered(json_file, currency = 'USD'):
    """Фильтрует транзакции по валюте и записывает новые данные в новый файл."""

    with open(json_file, encoding='utf-8') as new_file:
        file = json.load(new_file)

    # list_ = [file for file in file if file.get('currency') == currency]
    #
    #
    # with open('operations.json', 'w') as file:
    #     json.dump(list_, file, indent=4)
    return file

operation = 'operations.json'

result= transactions_filtered(operation)
print(result)
