class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        le=len(nums)
        l=[0]*(le)
        for i in range(2,le):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                l[i]=1+l[i-1]
        return sum(l)
solution = Solution()
print(solution.numberOfArithmeticSlices([1,2,3,4]))