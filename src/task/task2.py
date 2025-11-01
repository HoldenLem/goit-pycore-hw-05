import re
from typing import Callable, Generator

_NUMBER_PATTERN = re.compile(
    r"(?<=\s)\d+(?:\.\d+)?(?=\s)"
)


def generator_numbers(text: str):
    """
        Generate all valid floating-point numbers from the given text.
    """
    for m in _NUMBER_PATTERN.finditer(text):
        yield float(m.group())


def sum_profit(text: str, func: Callable):
    """
    Calculates the total sum
    """
    return sum(func(text))
