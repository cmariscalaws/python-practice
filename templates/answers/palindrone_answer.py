
from typing import List

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if(s[left].lower() != s[right].lower()):
            return False
        else:
            left += 1
            right -= 1

    return True

if __name__ == '__main__':
    case_1 = "a dog! a panic in a pagoda."
    case_2 = "abc123"
    case_3 = "A man, a plan, a canal: Panama"

    result1 = is_palindrome(case_1)
    expected = True
    print(f"Test 1: case = {case_1}, expected={expected}, result={result1}")
    assert result1 == expected, f"Expected {expected}, but got {result1}"

    result2 = is_palindrome(case_2)
    expected = False
    print(f"Test 2: case = {case_2}, expected={expected}, result={result2}")
    assert result2 == expected, f"Expected {expected}, but got {result2}"

    result3 = is_palindrome(case_3)
    expected = True
    print(f"Test 3: case = {case_3}, expected={expected}, result={result3}")
    assert result3 == expected, f"Expected {expected}, but got {result3}"
