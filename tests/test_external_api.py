from unittest.mock import patch

import pytest
import requests

from src.external_api import convert_to_rub


@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.HTTPError(f"HTTP ошибка: {self.status_code}")

    return MockResponse


def test_convert_to_rub():
    """Тест конвертации RUB в RUB"""
    transaction = {"amount": 100, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 100.0


@patch("external_api.requests.get")
def test_convert_to_rub(mock_get, mock_response):
    """Тест конвертации USD в RUB"""
    mock_get.return_value = mock_response({"result": 7500}, 200)

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rub(transaction)

    assert result == 7500.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub(mock_get, mock_response):
    """Тест конвертации EUR в RUB"""
    mock_get.return_value = mock_response({"result": 8500}, 200)

    transaction = {"amount": 100, "currency": "EUR"}
    result = convert_to_rub(transaction)

    assert result == 8500.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_http_error(mock_get, mock_response):
    """Тест обработки HTTP ошибки"""
    mock_get.return_value = mock_response({"error": "Ошибка API"}, 400)

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rub(transaction)

    assert result is None


@patch("src.external_api.requests.get")
def test_request_exception(mock_get):
    """Тест обработки исключения запроса"""
    mock_get.side_effect = requests.RequestException("Ошибка сети")

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rub(transaction)

    assert result is None
