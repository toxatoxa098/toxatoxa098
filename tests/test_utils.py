import json
import os
import tempfile

import pytest

from src.utils import operations  # Замените 'your_module' на имя вашего модуля


@pytest.fixture
def sample_json_file():
    """Фикстура для создания временного JSON файла"""
    sample_data = [{"id": 1, "name": "Операция 1"}, {"id": 2, "name": "Операция 2"}]
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as temp:
        json.dump(sample_data, temp)
    yield temp.name
    os.unlink(temp.name)


def test_operations_with_valid_json(sample_json_file):
    """Тест функции operations с корректным JSON файлом"""
    result = operations(sample_json_file)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["name"] == "Операция 2"


def test_operations_with_nonexistent_file():
    """Тест функции operations с несуществующим файлом"""
    result = operations("nonexistent_file.json")
    assert result == []


def test_operations_with_invalid_json(tmp_path):
    """Тест функции operations с некорректным JSON файлом"""
    invalid_json = tmp_path / "invalid.json"
    invalid_json.write_text("{invalid json", encoding="utf-8")
    result = operations(str(invalid_json))
    assert result == []


def test_operations_with_empty_file(tmp_path):
    """Тест функции operations с пустым файлом"""
    empty_file = tmp_path / "empty.json"
    empty_file.touch()
    result = operations(str(empty_file))
    assert result == []
