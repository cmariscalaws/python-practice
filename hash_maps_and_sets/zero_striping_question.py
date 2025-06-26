
from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    pass


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5], [6, 0, 6, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 0]]
    expectedResult = [[1,0,3,4,0],[0,0,0,0,0],[11,0,13,14,0],[0,0,0,0,0]]
    zero_striping(matrix)
    print(matrix)

    assert matrix == expectedResult, f"Expected {expectedResult}, but got {matrix}"
