from typing import List
from functools import reduce

class ReduceExamples:
    """
    The reduce function in Python applies a specified function cumulatively to the items of an iterable,
        reducing the iterable to a single value.

    In the `reduce` function, `x` is the accumulator (the running total or result so far),
        and `y` is the next item from the iterable. On the first call, `x` is the first element,
        and `y` is the second. On each subsequent call, `x` is the result of the previous lambda call,
        and `y` is the next element in the iterable. This process continues until all items are processed, r
        esulting in a single accumulated value.

    Parameters:
        function: A function that takes two arguments and returns a single value.
        iterable: An iterable (e.g., list, tuple) whose elements are combined.
        initializer (optional): A value that is placed before the items of the iterable in the calculation.

    Returns:
        A single value resulting from the cumulative application of the function to the iterable's items.

    Example:
        reduce(lambda x, y: x + y, [1, 2, 3, 4]) returns 10.

    Example with initializer:
        numbers = [1, 2, 3, 4]
        result = reduce(lambda x, y: x + y, numbers, 10)
        print(result)  # Output: 20

        Explanation:
            The sum starts at 10 (initializer), then adds each number in the list: 10 + 1 + 2 + 3 + 4 = 20.
    """
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def sum_of_numbers(self):
        return reduce(lambda x, y: x + y, self.numbers)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    expected = 15
    reduce_examples = ReduceExamples(numbers)
    result = reduce_examples.sum_of_numbers()
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"