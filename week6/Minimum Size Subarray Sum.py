class Solution(object):
    def minSubArrayLen(self, target, nums):
        if sum(nums) < target:
            return 0
        if max(nums) >= target:
            return 1
        left, right, current_sum = 0, 0, nums[0]
        min_size = len(nums) + 1
        while right < len(nums):
            if current_sum >= target:
                min_size = min(min_size, right - left + 1)
                current_sum -= nums[left]
                left += 1
            else:
                if right == len(nums) - 1:
                    break
                else:
                    right += 1
                    current_sum += nums[right]
        if min_size == len(nums) + 1:
            return 0
        else:
            return min_size
solution = Solution()
print(solution.minSubArrayLen(7,[2,3,1,2,4,3]))