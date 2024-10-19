class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        if len(nums)==0:
            return 0
        m = 1
        count = 1
        for i in range(len(nums)-1):
            if (nums[i+1]-nums[i])==1:
                count+=1
                m = max(m,count)
            elif (nums[i+1]-nums[i])==0:
                continue
            else:
                count = 1
        return m
solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))