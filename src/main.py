from filtering_by_given_parameters import (
    filter_transactions_by_currency,
    filter_transactions_by_status,
    load_transactions_from_csv,
    load_transactions_from_json,
    load_transactions_from_xlsx,
    search_transactions_by_description,
    sort_transactions_by_date,
    count_transactions_by_category,
)


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input()

        if choice == "1":
            transactions = load_transactions_from_json(
                r"C:\Users\Пользователь\PycharmProjects\pythonProject\src/transactions.json"
            )
            break
        elif choice == "2":
            transactions = load_transactions_from_csv(
                r"C:\Users\Пользователь\PycharmProjects\pythonProject\src\transactions.csv"
            )
            break
        elif choice == "3":
            transactions = load_transactions_from_xlsx(r"C:\Users\Пользователь\Downloads\transactions_excel (1).xlsx")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

    print(f"Для обработки выбран {'JSON' if choice == '1' else 'CSV' if choice == '2' else 'XLSX'}-файл.")

    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().upper()

        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_transactions_by_status(transactions, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == "да":
        sort_direction = input("Отсортировать по возрастанию или по убыванию? ").lower()
        transactions = sort_transactions_by_date(transactions, sort_direction == "по возрастанию")

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_choice == "да":
        transactions = filter_transactions_by_currency(transactions)

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if search_choice == "да":
        search_word = input("Введите слово для поиска: ").lower()
        transactions = search_transactions_by_description(transactions, search_word)
    if input("Подсчитать транзакции по категориям? (да/нет): ").lower() == "да":
        categories = input("Введите категории через запятую: ").split(",")
        categories = [category.strip() for category in categories]
        category_counts = count_transactions_by_category(transactions, categories)
        print("\nКоличество транзакций по категориям:")
        for category, count in category_counts.items():
            dict_ = {category: count}
            print(dict_)

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(transactions)}")

    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for t in transactions:
            from_account = t.get("from")
            to_account = t.get("to")

            parts_from = from_account.split()
            if len(parts_from) > 1:
                account_type_from = " ".join(parts_from[:-1])
                number_from = parts_from[-1]
                masked_number_from = f"{number_from[:4]} {number_from[4:6]}** **** {number_from[-4:]}"
            else:
                account_type_from = from_account
                masked_number_from = ""

            parts_to = to_account.split()
            if len(parts_to) > 1:
                account_type_to = " ".join(parts_to[:-1])
                number_to = parts_to[-1]
                masked_number_to = f"**{number_to[-4:]}"
            else:
                account_type_to = to_account
                masked_number_to = ""

            print(f"\n{t['date']} {t['description']}")
            if masked_number_from:
                print(f"{account_type_from} {masked_number_from} -> ", end="")
            else:
                print(f"{account_type_from} -> ", end="")

            print(f"{account_type_to} {masked_number_to}")
            print(f"Сумма: {t['amount']} {t.get('currency_code', '')} {t.get('currency_name', '')}")


if __name__ == "__main__":
    main()
