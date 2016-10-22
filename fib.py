fib_values = [1, 1]


def fib(n):
    try:
        return fib_values[n]
    except IndexError:
        fib_values.append(fib(n-1) + fib(n-2))
        return fib_values[n]


if __name__ == '__main__':
    for i in range(0, 100):
        print(fib(i))