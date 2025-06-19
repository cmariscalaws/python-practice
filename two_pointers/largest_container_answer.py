from typing import List

def largest_container(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    max_container = 0

    while left < right:
        distance = right - left
        container = min(heights[left], heights[right]) * distance

        if container > max_container:
            max_container = container

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return max_container

if __name__ == '__main__':
    heights =  [2, 7, 8, 3, 7, 6]
    expectedResult = 24

    result = largest_container(heights)

    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"

