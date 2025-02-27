import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def operations(json_file: str) -> List[Dict[str, Any]]:
    """Функция загружает данные из файла в JSON-формате и преобразует их в объект Python."""
    logger.info('Начало работы функции "operations"')
    try:
        with open(json_file, 'r', encoding="utf-8") as new_file:
            file = json.load(new_file)
            logger.info(f'Извлекаем данные из файла "operations.json" в json-формате: {file}')
            logger.info('Успешное завершение функции "operations"')
        return file

    except (FileNotFoundError, json.JSONDecodeError):
        logger.error('Проверка на ошибку: "JSONDecodeError" возвращает [] список')
        return []


path = r"C:\Users\Пользователь\PycharmProjects\pythonProject\data\operations.json"
result = operations(path)
print(result)
