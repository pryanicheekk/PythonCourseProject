class Solution(object):
    def setZeroes(self, matrix):
        help_row = []
        help_col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i not in help_row:
                        help_row.append(i)
                    if j not in help_col:
                        help_col.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in help_row or j in help_col:
                    matrix[i][j]=0
        return matrix
solution = Solution()
print(solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))