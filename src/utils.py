import json
from typing import Dict, List, Any


def operations(json_file: str) -> List[Dict[str, Any]]:
    """Функция загружает данные из файла в JSON-формате и преобразует их в объект Python."""
    try:
        with open(json_file, 'r', encoding="utf-8") as new_file:
            file = json.load(new_file)

        return file

    except (FileNotFoundError, json.JSONDecodeError):
        return []


path = r"C:\Users\Пользователь\PycharmProjects\pythonProject\data\operations.json"
result = operations(path)
print(result)
