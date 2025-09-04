from typing import List
from functools import reduce

class Chaining:
   def __init__(self, numbers: List[int]):
         self.numbers = numbers

   def process_numbers(self) -> int:
        pass


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    expected = 20  # 2^2 + 4^2 = 4 + 16 = 20
    chaining = Chaining(numbers)
    result = chaining.process_numbers()
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"