class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        pm,pn = m-1, n-1
        while pm>=0 and pn>=0:
            if matrix[pm][pn] == target:
                return True
            elif matrix[pm][pn]<target:
                return False
            else:
                if matrix[pm-1][pn]>=target and pm!=0:
                    pm-=1
                else:
                    pn-=1
        return False
solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))