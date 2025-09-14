
from typing import List

def is_palindrome_valid(s: str) -> bool:
    pass

if __name__ == '__main__':
    case_1 = "a dog! a panic in a pagoda."
    case_2 = "abc123"
    case_3 = "A man, a plan, a canal: Panama"

    result1 = is_palindrome_valid(case_1)
    print(result1)
    assert result1 == True, f"Expected {True}, but got {result1}"

    result2 = is_palindrome_valid(case_2)
    print(result2)
    assert result2 == False, f"Expected {False}, but got {result2}"

    result3 = is_palindrome_valid(case_3)
    print(result3)
    assert result3 == True, f"Expected {True}, but got {result3}"
