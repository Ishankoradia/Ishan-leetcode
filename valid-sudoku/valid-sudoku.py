class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_list = [[] for _ in range(9)]
        row_list = [[] for _ in range(9)]
        b_list = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                s = board[i][j]
                if s != ".":
                    b = i // 3 + j // 3 + 2 * (i // 3)
                    if s in col_list[j] or s in row_list[i] or s in b_list[b]:
                        return False
                    else:
                        col_list[j].append(s)
                        row_list[i].append(s)
                        b_list[b].append(s)
        return True
            
                