import csv
import json
import re
from collections import Counter
from datetime import datetime
from typing import Any, Dict, List

import openpyxl


def search_transactions_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Функция для поиска по описанию с использованием регулярных выражений"""

    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction["description"])]


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Функция подсчета транзакций по категориям"""

    lower_categories = {category.lower(): category for category in categories}

    category_counter = Counter()

    for transaction in transactions:
        description = transaction["description"].lower()
        for lower_category in lower_categories:
            if lower_category in description:
                category_counter[lower_categories[lower_category]] += 1

    return {category: category_counter[category] for category in categories}


def load_transactions_from_json(filename: str) -> List[Dict[str, Any]]:
    """Функция обрабатывает данные из файла json-формата и возвращает объект Python(список словарей)."""

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def load_transactions_from_csv(filename: str) -> List[Dict[str, Any]]:
    """Функция обрабатывает данные из CSV-файла и возвращает список словарей."""

    transactions = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            transactions.append(row)
    return transactions


def load_transactions_from_xlsx(filename: str) -> List[Dict[str, Any]]:
    """Функция обрабатывает данные из XLSX-файла и возвращает список словарей."""

    transactions = []
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active
    headers = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        transaction = {headers[i]: value for i, value in enumerate(row)}
        transactions.append(transaction)
        # print(transactions)
    return transactions


def filter_transactions_by_status(transactions: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """Функция фильтрует транзакции по статусу."""

    return [t for t in transactions if t["state"] is not None if t.get("state").upper() == status.upper()]


def sort_transactions_by_date(transactions: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """Функция сортирует транзакции по дате(в порядке убывания и в порядке возрастания)."""

    return sorted(
        transactions, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%SZ"), reverse=not ascending
    )


def filter_transactions_by_currency(transactions: List[Dict[str, Any]], currency: str = "RUB") -> List[Dict[str, Any]]:
    """Функция фильтрует транзакции по коду валюты."""

    return [t for t in transactions if t.get("currency_code") == currency]
