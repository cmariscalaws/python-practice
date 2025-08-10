
from typing import List

bad_version = 0

def is_bad_version(n: int) -> bool:
    if n == bad_version:
        return True
    else:
        return False

def first_bad_version(n: int) -> int:
    left, right = 1, n
    result = -1

    while left <= right:
        mid = (left + right) // 2
        result = is_bad_version(mid)

        if result == True:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

if __name__ == '__main__':
    bad_version = 4
    expected = 4
    result = first_bad_version(5)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"

    bad_version = 1
    expected = 1
    result = first_bad_version(1)
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"


