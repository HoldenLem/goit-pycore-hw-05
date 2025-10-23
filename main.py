from task.task1 import caching_fibonacci


def main():
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(15))



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
