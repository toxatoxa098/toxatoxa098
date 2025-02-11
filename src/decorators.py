from functools import wraps


def log(filename=None):
    """Декоратор для логирования вызовов функций."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Оберточная функция, которая выполняет логирование."""

            log_message = f"{func.__name__} "
            try:
                result = func(*args, **kwargs)
                log_message += "ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as e:
                error_message = f"error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                log_message += error_message
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message + "\n")
                else:
                    print(log_message)
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция суммирует два числа."""

    return x + y


my_function(1, 8)
