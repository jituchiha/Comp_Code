
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Only solution
    # Check for all of the 3 conditions. Key part here is to //3 to check if a number is present in that particular square and if it is then return False or else you can check for other conditions and finally return True
    # 1
    # 1
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)

        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue

                if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3, c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

                squares[(r//3,c//3)].add(board[r][c])

        return True
                


