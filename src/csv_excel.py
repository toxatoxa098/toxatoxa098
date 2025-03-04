import csv
from typing import Dict, List, Union

import pandas as pd


def csv_format(file_csv: str) -> Union[List[Dict[str, str]], str]:
    """Функция для считывания финансовых операций из файла-CSV возвращает список словарей с транзакциями."""

    try:
        with open(file_csv, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            list_of_dict = []
            for row in reader:
                list_of_dict.append(row)
            return list_of_dict
    except FileNotFoundError:
        return 'Ошибка: "FileNotFoundError"'


path = r"C:\Users\Пользователь\Downloads\transactions.csv"
result = csv_format(path)
print(result)


def excel_format(file_excel: str) -> Union[List[Dict[str, Union[str, int, float]]], str]:
    """Функция для считывания финансовых операций из файла-EXCEL возврвщает список словарей с транзакциями."""

    try:
        df = pd.read_excel(file_excel)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return 'Ошибка: "FileNotFoundError"'


path = r"C:\Users\Пользователь\Downloads\transactions_excel.xlsx"
result = excel_format(path)
print(result)


    # Здесь можно добавить дополнительные проверки структуры данных
