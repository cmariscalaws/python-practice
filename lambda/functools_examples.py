from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Output: 55

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))  # Output: 10

from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

from functools import cmp_to_key

def compare(x, y):
    return x - y

numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
print(sorted_numbers)  # Output: [1, 2, 5, 9]

from functools import total_ordering

@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

a = Number(3)
b = Number(5)
print(a <= b)  # Output: True
print(a > b)   # Output: False



