import math


def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a


def multiplication(a, b):
    c = a * b
    return c


def division(a, b):
    a = int(a)
    b = int(b)
    return round(b / a, 7)


def square(a):
    a = int(a)
    return a ** 2


def root(a):
    a = int(a)
    return round(math.sqrt(a), 8)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = round(division(a, b), 7)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = root(a)
        return self.result
