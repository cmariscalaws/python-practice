from typing import List
from functools import reduce

class ChainingExamples:
   def __init__(self, numbers: List[int]):
         self.numbers = numbers

   def process_numbers(self) -> int:
        """
        Processes self.numbers by filtering even numbers, squaring them, and sorting the results.

        Steps:
        1. Filter even numbers using filter with a lambda function.
        2. Square each filtered number using map with a lambda function.
        3. Sum the squared numbers.

        Returns:
            A sum of squared even numbers.
        """
        return reduce(lambda x,y: x+y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, self.numbers)))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    expected = 20  # 2^2 + 4^2 = 4 + 16 = 20
    chaining_examples = ChainingExamples(numbers)
    result = chaining_examples.process_numbers()
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"