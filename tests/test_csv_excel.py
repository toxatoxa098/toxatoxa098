from io import StringIO
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.csv_excel import csv_format, excel_format


@pytest.fixture
def sample_csv_content():
    return "date;description;amount\n" "2023-05-01;Покупка продуктов;100.50\n" "2023-05-02;Оплата счета;200.75\n"


@patch("src.csv_excel.open")
def test_csv_format(mock_open, sample_csv_content):
    mock_open.return_value.__enter__.return_value = StringIO(sample_csv_content)

    result = csv_format("dummy.csv")

    assert len(result) == 2
    assert result[0] == {"date": "2023-05-01", "description": "Покупка продуктов", "amount": "100.50"}
    assert result[1] == {"date": "2023-05-02", "description": "Оплата счета", "amount": "200.75"}

    mock_open.assert_called_once_with("dummy.csv", encoding="utf-8")


@patch("src.csv_excel.open")
def test_csv_format_empty_file(mock_open):
    mock_open.return_value.__enter__.return_value = StringIO("date;description;amount\n")
    result = csv_format("empty.csv")
    assert result == []


@patch("src.csv_excel.open")
def test_csv_format_file_not_found(mock_open):
    mock_open.side_effect = FileNotFoundError
    result = csv_format("non_existent.csv")
    assert result == 'Ошибка: "FileNotFoundError"'


@pytest.fixture
def sample_excel_data():
    return pd.DataFrame(
        {
            "date": ["2023-05-01", "2023-05-02"],
            "description": ["Покупка продуктов", "Оплата счета"],
            "amount": [100.50, 200.75],
        }
    )


@patch("pandas.read_excel")
def test_excel_format_success(mock_read_excel, sample_excel_data):
    mock_read_excel.return_value = sample_excel_data

    result = excel_format("dummy.xlsx")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"date": "2023-05-01", "description": "Покупка продуктов", "amount": 100.50}
    assert result[1] == {"date": "2023-05-02", "description": "Оплата счета", "amount": 200.75}

    mock_read_excel.assert_called_once_with("dummy.xlsx")


@patch("pandas.read_excel")
def test_excel_format_empty_file(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame()

    result = excel_format("empty.xlsx")

    assert isinstance(result, list)
    assert len(result) == 0

    mock_read_excel.assert_called_once_with("empty.xlsx")


@patch("pandas.read_excel")
def test_excel_format_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError

    result = excel_format("non_existent.xlsx")

    assert result == 'Ошибка: "FileNotFoundError"'

    mock_read_excel.assert_called_once_with("non_existent.xlsx")


def test_excel_format_integration():
    # Этот тест использует реальный файл. Убедитесь, что путь корректен
    path = r"C:\Users\Пользователь\Downloads\transactions_excel.xlsx"
    result = excel_format(path)

    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(item, dict) for item in result)
