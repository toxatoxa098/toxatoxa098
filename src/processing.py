from typing import Any, Dict, List


def filter_by_state(list_: List[Dict[str, Any]], default_parameter: str = "EXECUTED") -> list:
    """Функция, принимает список словарей и опционально значение для
    ключа state(по умолчанию 'EXECUTED'). Функция возвращает новый
    список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""

    new_list = []
    for key in list_:
        if key.get("state") == default_parameter:
            new_list.append(key)
    return new_list


def sort_by_date(list_: List[Dict[str, Any]], default_parameter: bool = True) -> list:
    """Функция, принимает список словарей и необязательный
    параметр, задающий порядок сортировки (по умолчанию — убывание) и возвращает
     новый список, отсортированный по дате (date)."""

    return sorted(list_, key=lambda element: element.get("date",'0'), reverse=not default_parameter)


result = filter_by_state(
    [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)
print(result)
result = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018.10.14T08:21:33.419441"},
    ]
)
print(result)
