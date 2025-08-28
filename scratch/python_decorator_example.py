import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} returned {result} took {end - start} seconds to run")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

if __name__ == '__main__':
    add(1, 2)