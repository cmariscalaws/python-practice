from typing import List


class Map(object):
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def square(self) -> List[int]:
        pass

if __name__ == '__main__':

    numbers = [1, 2, 3, 4, 5]
    mapping = Map(numbers)
    squared_numbers = mapping.square()

    assert squared_numbers == [1, 4, 9, 16, 25], f"Expected [1, 4, 9, 16, 25], but got {squared_numbers}"

    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)