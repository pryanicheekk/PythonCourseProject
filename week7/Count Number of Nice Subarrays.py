class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        l = 0
        r = 0
        res = 0

        while r < n:
            while r < n and k > 0:
                if nums[r] % 2 != 0:
                    k -= 1
                r += 1
            i = l
            j = r
            while l < r and nums[l] % 2 == 0:
                l += 1
            while r < n and nums[r] % 2 == 0:
                r += 1
            if k == 0:
                res += (l - i + 1) * (r - j + 1)
            l += 1
            k += 1
        return res
solution = Solution()
print(solution.numberOfSubarrays([1,1,2,1,1],3))