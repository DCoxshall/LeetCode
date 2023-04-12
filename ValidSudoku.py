class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            nums = [int(a) for a in row if a != "."]
            if sorted(list(set(nums))) != sorted(nums):
                return False

        # Check columns
        for col in range(9):
            column = [board[i][col] for i in range(9)]
            nums = [int(a) for a in column if a != "."]
            if sorted(list(set(nums))) != sorted(nums):
                return False
        
        # Check sub-grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[i + a][j + b] for a in range(0, 3) for b in range(0, 3)]
                nums = [int(a) for a in subgrid if a != "."]
                if sorted(list(set(nums))) != sorted(nums):
                    return False

        return True
