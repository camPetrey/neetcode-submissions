class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        #Check each row if valid
        for row in range(rows):
            seen = set()
            for col in range(cols):
                if board[row][col] == ".":
                    continue
                num = board[row][col]
                if num in seen:
                    return False
                seen.add(num)

        #Check each col if valid
        for col in range(cols):
            seen = set()
            for row in range(rows):
                num = board[row][col]
                if board[row][col] == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        #Check Squares
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True






