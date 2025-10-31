from src.task.task2 import generator_numbers, sum_profit

SILY_TEXT = " 340 50.00 0.90 "


def test_valid_generator_numbers():
    sily_generator = generator_numbers(SILY_TEXT)
    assert next(sily_generator) == 340
    assert next(sily_generator) == 50.00
    assert next(sily_generator) == 0.90


def test_sum_profit():
    assert sum_profit(SILY_TEXT, generator_numbers) == 390.90
