from typing import List

class Filter:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def filter_even(self) -> List[int]:
        pass

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    expected = [2, 4, 6]
    filtering = Filter(numbers)
    result = filtering.filter_even()
    print(result)
    assert result == expected, f"Expected {expected}, but got {result}"