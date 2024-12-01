class Solution(object):
    def minOperations(self, nums, x):
        totalSum = sum(nums)
        target = totalSum - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        n = len(nums)
        minOperations = float('inf')
        currentSum = 0
        leftIndex = 0
        rightIndex = 0
        while rightIndex < n:
            currentSum += nums[rightIndex]
            rightIndex += 1
            while currentSum > target and leftIndex < n:
                currentSum -= nums[leftIndex]
                leftIndex += 1
            if currentSum == target:
                minOperations = min(minOperations, n - (rightIndex - leftIndex))

        if minOperations == float('inf'):
            return -1
        else:
            return minOperations
solution = Solution()
print(solution.minOperations([1,1,4,2,3],5))