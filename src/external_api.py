import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму
       транзакции (amount) в рублях, тип данных — float."""

    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)

    params = {"from": currency, "to": "RUB", "amount": amount}

    headers = {"apikey": API_KEY}
    try:
        response = requests.get(BASE_URL, params=params, headers=headers)
        response.raise_for_status()
        result = response.json()
        return float(result["result"])
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    return None


if __name__ == "__main__":
    transaction_usd = {"amount": 100, "currency": "USD"}

    # Вызов функции для конвертации USD в RUB
    result_usd = convert_to_rub(transaction_usd)
    if result_usd is not None:
        print(f"100 USD = {result_usd:.2f} RUB")
    else:
        print("Failed to convert USD to RUB")

    transaction_eur = {"amount": 100, "currency": "EUR"}

    # Вызов функции для конвертации EUR в RUB
    result_eur = convert_to_rub(transaction_eur)
    if result_eur is not None:
        print(f"100 EUR = {result_eur:.2f} RUB")
    else:
        print("Failed to convert EUR to RUB")
