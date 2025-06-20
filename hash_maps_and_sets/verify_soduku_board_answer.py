
from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    # initialize row_sets
    row_sets = [set() for _ in range(9)]
    # initialize column_sets
    column_sets = [set() for _ in range(9)]
    # initialize sub_grid_sets
    sub_grid_sets = [[set() for _ in range(3)] for _ in range(3)]

    # iterate over row
    for r in range(9):
        # iterate over column
        for c in range(9):
            #get num from board [r][c]
            num = board[r][c]
            print(num)

            #if num is 0 continue
            if num == 0:
                continue

            # check num is in row_sets return false
            if num in row_sets[r]:
                return False

            # check num is in colum_sets return false
            if num in column_sets[c]:
                return False

            # check num is in sub_grid_sets return false
            if num in sub_grid_sets[r // 3 ][c // 3]:
                return False

            # add num to row_sets
            row_sets[r].add(num)

            # add num to column_sets
            column_sets[c].add(num)

            # add num to sub_group_sets
            sub_grid_sets[r // 3][c // 3].add(num)

    # all checks pass return true
    return True


if __name__ == '__main__':
    board = [[3,0,6,0,5,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[1,0,2,5,0,0,3,2,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[0,1,0,0,0,0,0,7,4],[0,3,0,0,0,8,2,5,0],[0,0,5,2,0,6,0,0,0]]
    expectedResult = False
    result = verify_sudoku_board(board)

    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"


    board = [[3,0,6,0,5,2,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1],[1,0,2,5,0,0,3,4,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[0,1,0,0,0,0,0,7,4],[0,3,0,0,0,8,2,5,0],[0,0,5,2,0,6,0,0,0]]
    expectedResult = True
    result = verify_sudoku_board(board)

    print(result)
    assert result == expectedResult, f"Expected {expectedResult}, but got {result}"
