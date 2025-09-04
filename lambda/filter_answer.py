from typing import List

class Filter:
    """
    The filter function in Python constructs an iterator from elements of an iterable for which a provided function returns True.

    Parameters:
        function: A function that returns True or False for each element.
        iterable: An iterable (e.g., list, tuple) whose elements are tested.

    Returns:
        An iterator yielding only those elements for which the function returns True.

    Example:
        filter(lambda x: x > 0, [-1, 0, 1, 2]) yields 1, 2.
        To get a list, use list(filter(lambda x: x > 0, [-1, 0, 1, 2])) which returns [1, 2].
    """
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    @staticmethod
    def is_even(x: int) -> bool:
        return x % 2 == 0


    """
    Returns a list of even numbers from self.numbers.

    Uses the built-in filter function with a lambda that checks if each number is divisible by 2 (x % 2 == 0).
    Only numbers for which the lambda returns True (i.e., even numbers) are included in the result.
    """
    def filter_even(self) -> List[int]:
        return list(filter(lambda x: Filter.is_even(x), self.numbers))

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    expected = [2, 4, 6]
    filtering = Filter(numbers)
    result = filtering.filter_even()
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"