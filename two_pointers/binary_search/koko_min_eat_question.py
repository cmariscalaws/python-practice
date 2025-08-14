import math
from typing import List


def can_finish(piles: List[int], h: int, k: int) -> bool:
    pass

def min_eating_speed(piles: List[int], h: int) -> int:
    pass

if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    expected = 4
    result = min_eating_speed(piles, h)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    piles = [30, 11, 23, 4, 20]
    h = 5
    expected = 30
    result = min_eating_speed(piles, h)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    piles = [30, 11, 23, 4, 20]
    h = 6
    expected = 23
    result = min_eating_speed(piles, h)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"
