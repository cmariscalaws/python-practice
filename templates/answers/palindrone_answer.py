
from typing import List

def is_palindrome_valid(s: str) -> bool:
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

    result1 = is_palindrome_valid(case_1)
    print(result1)
    assert result1 == True, f"Expected {True}, but got {result1}"

    result2 = is_palindrome_valid(case_2)
    print(result2)
    assert result2 == False, f"Expected {False}, but got {result2}"

    result3 = is_palindrome_valid(case_3)
    print(result3)
    assert result3 == True, f"Expected {True}, but got {result3}"
