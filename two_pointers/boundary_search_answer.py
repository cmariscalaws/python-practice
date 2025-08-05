
from typing import List

def find_boundary(arr: List[bool]) -> int:
    pass

if __name__ == '__main__':
    arr = [False, False, True, True, True]
    expected = 2
    result = find_boundary(arr)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [True]
    expected = 0
    result = find_boundary(arr)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [False, False, False]
    expected = -1
    result = find_boundary(arr)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [True, True, True, True, True]
    expected = 0
    result = find_boundary(arr)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [False, True]
    expected = 1
    result = find_boundary(arr)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [False, False, False, False, False, False, False, False, True]
    expected = 8
    result = find_boundary(arr)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"
