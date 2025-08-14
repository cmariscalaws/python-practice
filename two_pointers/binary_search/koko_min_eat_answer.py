import math
from typing import List


def can_finish(piles: List[int], h: int, k: int) -> bool:
    # Determines if Koko can finish eating all the bananas in 'piles' within 'h' hours,
    # given an eating speed of 'k' bananas per hour.
    hours_used = 0
    for pile in piles:
        # For each pile, calculate the hours needed at speed 'k' (rounding up).
        hours_used += math.ceil(float(pile) / k)
    # Return True if total hours used is within the allowed hours 'h'.
    return hours_used <= h

def min_eating_speed(piles: List[int], h: int) -> int:
    # Uses binary search to find the minimum eating speed 'k' such that Koko can
    # finish all bananas in 'piles' within 'h' hours.
    left, right = 1, 1000000000  # Search range for possible speeds.
    result = -1
    while left <= right:
        mid = (left + right) // 2
        # Check if Koko can finish at speed 'mid'.
        if can_finish(piles, h, mid):
            result = mid      # Update result if possible.
            right = mid - 1   # Try to find a smaller valid speed.
        else:
            left = mid + 1    # Increase speed if not possible.
    # Return the minimum valid eating speed.
    return result

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
