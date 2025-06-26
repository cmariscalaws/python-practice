
from typing import List

"""
    Modifies the input matrix such that if an element is 0,
    its entire row and column are set to 0.
    
    Args:
       matrix: 2D list of integers
"""
def zero_striping(matrix: List[List[int]]) -> None:
    # validate to exist early
    if not matrix or not matrix[0]:
        return

    zero_rows = set()
    zero_columns = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):

            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_columns.add(c)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):

            if r in zero_rows:
                matrix[r][c] = 0

            if c in zero_columns:
                matrix[r][c] = 0


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5], [6, 0, 6, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 0]]
    expectedResult = [[1,0,3,4,0],[0,0,0,0,0],[11,0,13,14,0],[0,0,0,0,0]]
    zero_striping(matrix)
    print(matrix)

    assert matrix == expectedResult, f"Expected {expectedResult}, but got {matrix}"
