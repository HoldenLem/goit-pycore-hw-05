from task.task1 import caching_fibonacci
from task.task2 import sum_profit, generator_numbers


def main():
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(15))

    text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
if __name__ == '__main__':
    main()
