# Банковские операции

Этот проект представляет собой набор функций для работы с банковскими операциями.

## Функциональность

Проект включает в себя пять основных функций:

1. `filter_by_state(operations, state='EXECUTED')`: Фильтрует список банковских операций по их состоянию.
2. `sort_by_date(operations, reverse=True)`: Сортирует список банковских операций по дате.
3. `filter_by_currency(transactions, code= 'USD')`: Функция, принимает на вход список словарей, представляющих транзакции и возвращает
    генератор, который поочередно выдает транзакции, где валюта операции соответствует
    заданной (например, USD).
4. `transaction_descriptions(transactions)`: Функция, принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
5. `card_number_generator(start: int, end: int)`: Генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты.

## Декоратор log

Проект также включает декоратор `log` для автоматического логирования выполнения функций.

### Особенности декоратора log:

- Принимает необязательный аргумент `filename` для определения места записи логов.
- Если `filename` задан, логи записываются в указанный файл.
- Если `filename` не задан, логи выводятся в консоль.
- Логирует имя функции и результат выполнения при успешной операции.
- При возникновении ошибки логирует имя функции, тип ошибки и входные параметры.

### Пример использования декоратора:

python
from decorators import log

@log(filename="mylog.txt")
def myfunction(x, y):
    return x + y

myfunction(1, 2)

## Установка

Для использования этого проекта, клонируйте репозиторий:


git clone https://github.com/your-username/bank-operations.git
cd bank-operations


## Использование

Пример использования функций:


from bank_operations import filter_by_state, sort_by_date

# Предположим, у нас есть список операций
operations = [
    {"id": 1, "state": "EXECUTED", "date": "2023-05-15"},
    {"id": 2, "state": "CANCELED", "date": "2023-05-14"},
    {"id": 3, "state": "EXECUTED", "date": "2023-05-16"}
]

# Фильтрация выполненных операций
executed_operations = filter_by_state(operations)
print(executed_operations)

# Сортировка операций по дате (от новых к старым)
sorted_operations = sort_by_date(operations)
print(sorted_operations)


## Тестирование

Проект включает набор автоматических тестов для проверки корректности работы основных функций.

### Запуск тестов

Для запуска тестов выполните следующую команду в корневой директории проекта:


pytest

### Описание тестов

Основные тестовые сценарии включают:

1. **Тесты функции filter_by_state:**
   - Проверка фильтрации по статусу "EXECUTED"
   - Проверка фильтрации по статусу "CANCELED"
   - Параметризованный тест для проверки различных статусов
   - Проверка работы функции при отсутствии словарей с указанным статусом
   - Обработка списка без ключа 'state'

2. **Тесты функции sort_by_date:**
   - Сортировка по убыванию (default_parameter=False)
   - Сортировка по возрастанию (default_parameter=True)
   - Проверка корректности сортировки при одинаковых датах

3. **Тесты функции get_date:**
   - Проверка форматирования строки даты
   
4. **Тесты функции mask_account_card:**
   - Проверка маскировки номера счета
   - Проверка маскировки номера карты
   - Параметризованный тест для проверки различных входных данных

5. **Тесты функции filter_by_state:**
   - Проверка фильтрации по статусу "EXECUTED"
   - Проверка фильтрации по статусу "CANCELED"
   - Параметризованный тест для проверки различных статусов
   - Проверка работы функции при отсутствии словарей с указанным статусом
   - Обработка списка без ключа 'state'

6. **Тесты функции sort_by_date:**
   - Сортировка по убыванию (default_parameter=False)
   - Сортировка по возрастанию (default_parameter=True)
   - Проверка корректности сортировки при одинаковых датах
7. **Тесты функции get_mask_card_number:**
   - Проверка маскировки стандартного номера карты
   - Проверка маскировки номера карты с разделителями
   - Проверка маскировки номера карты с нестандартными символами
   - Проверка маскировки короткого номера карты
   - Обработка пустой строки
   - Обработка строки без цифр

8. **Тесты функции get_mask_account:**
   - Проверка маскировки стандартного номера счета
   - Проверка маскировки номера счета с нестандартными символами
   - Проверка маскировки номера счета с пробелами
   - Проверка маскировки номера счета с дефисами
   - Проверка маскировки короткого номера счета
   - Обработка пустой строки
   - Обработка строки без цифр
   
9. **Тесты функции filter_by_currency:**
   - Тесты, проверяющие, что функция корректно фильтрует транзакции по заданной валюте
   - Проверка, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют
   - Проверка, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций

10. **Тесты функции transaction_descriptions:**
    - Проверка, что функция возвращает корректные описания для каждой транзакции
    - Тестируйте работу функции с различным количеством входных транзакций, включая пустой список

11. **Тесты функции card_number_generator:**
    - Тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне
    - Проверка на корректность форматирования номеров карт
    - Проверка, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию

12. **Тесты декоратора log:**
    - Проверка записи логов в файл при успешном выполнении функции
    - Проверка вывода логов в консоль, когда файл не указан
    - Проверка обработки и логирования исключений
    - Проверка сохранения метаданных декорируемой функции


### Особенности тестов:

- Использование фикстур для подготовки тестовых данных
- Параметризация тестов для проверки различных сценариев
- Проверка граничных случаев и нестандартных ситуаций
- Использование аннотаций типов (Union[str]) для улучшения типизации

### Особенности тестов:

- Использование фикстур (filter_state, sort_date, sort_double_date, filter_no_state_1, filter_no_state_2) для подготовки тестовых данных
- Параметризация тестов для проверки различных сценариев
- Проверка граничных случаев и нестандартных ситуаций

### Покрытие кода

Для проверки покрытия кода тестами используйте команду:


pytest --cov=src

Текущее покрытие тестами составляет 93%.

### Дополнительная информация

- Тесты расположены в директории `tests/`
- Для мокирования и создания фикстур используется pytest
- При добавлении новых функций или изменении существующих, убедитесь, что соответствующие тесты обновлены или добавлены





## Разработка

Этот проект разрабатывается с использованием Git и GitHub. Основная разработка ведется в ветке `develop`, а новые функции разрабатываются в отдельных ветках с префиксом `feature`.

## Контрибьюция

Если вы хотите внести свой вклад в проект, пожалуйста, создайте pull request в ветку `develop`.

## Лицензия

[MIT](https://choosealicense.com/licenses/mit/)


Этот README файл содержит основную информацию о проекте, включая его функциональность, инструкции по установке и использованию, а также информацию о разработке и контрибьюции. Вы можете дополнить его дополнительными разделами или информацией по мере необходимости.