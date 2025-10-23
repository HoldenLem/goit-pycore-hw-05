import time
from collections.abc import Callable
from curses import wrapper
from functools import wraps


def main():
    def repeat(times: int):
        def decorator(func):
            @wraps(func)
            def inner(name: str):
                calls = []
                for i in range(times):
                    result = func(name)
                    calls.append(result)
                print("функція викликалась")
                return calls[-1]
            return inner

        return decorator

    def decoratorr(func):
        @wraps(func)
        def inner(name: str):
            result = func(name)
            print("функція викликалась")
            return result
        return inner

    @repeat(times=5)
    def hello(name):
        print(f"hi, {name}")
        return name

    assert hello("Ana") == "Ana"



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
