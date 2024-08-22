# compose
def square(x):
    return x * x


def successor(x):
    return x + 1


def compose(f, g):
    def h(x):
        return f(g(x))

    return h


square_successor = compose(square, successor)
x = square_successor(10)
print(x)


# newton method nth square root
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-15) -> bool:
    return abs(x - y) < tolerance


def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)

    return update


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):
    def f(x):
        return x * x - a

    def df(x):
        return 2 * x

    return find_zero(f, df)


def power(x, n):
    product = 1
    k = 0
    while k < n:
        product *= x
        k = k + 1

    return product


def nth_root_newton(n, a):
    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n - 1)

    return find_zero(f, df)


x = square_root_newton(64)
print(x)

x = nth_root_newton(3, 64)
print(x)

x = nth_root_newton(6, 64)
print(x)


# currying
def curry_power(x):
    def h(y):
        return pow(x, y)

    return h


curry_power(2)(3)


def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1


map_to_range(0, 10, curry_power(2))


# lambda expression
def compose_lambda(f, g):
    return lambda x: f(g(x))


f = compose_lambda(lambda x: x * x, lambda y: y + 1)

square_lambda = lambda x: x * x
square_lambda(12)


# function decorator
def trace(fn):
    def wrapped(x):
        print("->", fn, "(", x, ")")
        return fn(x)

    return wrapped


@trace
def triple(x):
    return 3 * x


x = triple(12)
print(x)


# recursive function
def sum_digits(x):
    if x < 10:
        return x
    else:
        last = x % 10
        others = x // 10
        return sum_digits(others) + last


print(sum_digits(18117))
