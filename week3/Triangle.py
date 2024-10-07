class Solution(object):
    def minimumTotal(self, triangle):
        for i in range(len(triangle)-1,0,-1):
            x=triangle[i]
            for j in range(len(x)-1):
                triangle[i-1][j]+=min(triangle[i][j],triangle[i][j+1])
        return triangle[0][0]
solution = Solution()
print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))