class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])

        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] in seen:
                            return False
                        else:
                            seen.add(board[r][c])
        
        return True
