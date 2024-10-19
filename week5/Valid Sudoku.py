class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            string = ''
            for j in range(9):
                if (board[i][j] in string) and (board[i][j]!='.'):
                    return False
                elif board[i][j]!='.':
                    string+=board[i][j]
                else:
                    continue
        for i in range(9):
            column = ''
            for j in range(9):
                if (board[j][i] in column) and (board[j][i]!='.'):
                    return False
                elif board[j][i]!='.':
                    column+=board[j][i]
                else:
                    continue
        help = [[3,3],[3,6],[3,9],[6,3],[6,6],[6,9],[9,3],[9,6],[9,9]]
        count=0
        while count<=8:
            square = ''
            for i in range(help[count][0]-3,help[count][0]):
                for j in range(help[count][1]-3,help[count][1]):
                    if (board[i][j] in square) and (board[i][j]!='.'):
                        return False
                    elif board[i][j]!='.':
                        square+=board[i][j]
                    else:
                        continue
            count+=1
        return True
solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))