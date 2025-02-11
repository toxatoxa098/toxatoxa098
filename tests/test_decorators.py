import pytest

from src.decorators import log


def test_log_to_console(capsys):
    @log(filename=None)
    def my_function(x, y):

        return x + y

    my_function(1, 8)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_to_file(test_file):
    @log(filename=str(test_file))
    def my_function(x, y):
        return x + y

    result = my_function(1, 8)
    assert result == 9

    with open(test_file, "r") as f:
        log_content = f.read()

    assert "my_function ok\n" in log_content


def test_log_exception_to_console(capsys):
    @log()
    def my_function(x, y):
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        my_function(1, 'j')

    captured = capsys.readouterr()
    assert "my_function error: ValueError. Inputs: (1, 'j'), {}\n" in captured.out
    assert "my_function error: ValueError. Inputs: (1, 'j'), {}\n" in captured.out
