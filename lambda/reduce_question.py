from typing import List
from functools import reduce

class Reduce:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def sum_of_numbers(self):
        pass

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    expected = 15
    reducing = Reduce(numbers)
    result = reducing.sum_of_numbers()
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"