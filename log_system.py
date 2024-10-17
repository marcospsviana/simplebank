import logging
from functools import wraps

logging.basicConfig(
    filename="simplebank.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)


def log_transaction(func):
    # @wraps
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"{(func.__name__).upper()} {args} {kwargs}")
        return result

    return wrapper
