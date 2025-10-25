import re
from typing import Iterable, Callable


def generator_numbers(text: str) :
    """
        Generate all valid floating-point numbers from the given text.
    """
    for t in text.split():
        if income(t):
            yield float(t)


def sum_profit(text: str, func: Callable):
    """
    Calculates the total sum
    """
    return sum(func(text))


def income(text_element: str) -> bool:
    """
        Checks if the text element is a valid number (integer or decimal with up to 2 digits after the dot).
    """
    if re.match(r'^(?:0|[1-9]\d*)(?:\.\d{1,2})?$', text_element):
        return True
    return False
