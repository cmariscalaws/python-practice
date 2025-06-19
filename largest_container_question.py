from typing import List

def largest_container(heights: List[int]) -> int:
    pass

if __name__ == '__main__':
    heights =  [2, 7, 8, 3, 7, 6]
    expectedResult = 24

    result = largest_container(heights)

    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"

