from itertools import permutations
class Solution(object):
    def permute(self, nums):
        return list(permutations(nums))
solution = Solution()
print(solution.permute([1,2,3]))

