
from typing import List

picked_number = 6

def guess(n: int) -> int:
    if n == picked_number:
        return 0
    elif n < picked_number:
        return 1
    else:
        return -1

def guess_number(n: int) -> int:
    pass

if __name__ == '__main__':
    expected = 6
    result = guess_number(10)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"


